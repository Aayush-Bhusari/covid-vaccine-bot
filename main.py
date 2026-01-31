import tweepy
import requests
from datetime import datetime
import time
import schedule

# Configuration
# Replace these placeholders with environment variables or keep them empty for security
CONSUMER_KEY = "YOUR_CONSUMER_KEY"
CONSUMER_SECRET = "YOUR_CONSUMER_SECRET"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"

mh_district_ids = [397] # Aurangabad District ID
COWIN_URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict"

def data_from_cowin(district_id):
    now = datetime.now()
    today_date = now.strftime("%d-%m-%Y")
    query_params = f"?district_id={district_id}&date={today_date}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    final_url = COWIN_URL + query_params
    try:
        response = requests.get(final_url, headers=headers)
        if response.status_code == 200:
            extract_availability_data(response.json())
    except Exception as e:
        print(f"Error fetching data: {e}")

def fetch_data_for_state(district_ids):
    for district_id in district_ids:
        data_from_cowin(district_id)

def extract_availability_data(response_json):
    # Setup Twitter API
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    for center in response_json.get("centers", []):
        for session in center.get("sessions", []):
            if session["available_capacity_dose1"] > 0 and session["available_capacity_dose2"] > 0:
                message = (
                    f"<<<Vaccine Alert>>>\n\n"
                    f"Date: {session['date']}\n"
                    f"Pincode: {center['pincode']}\n"
                    f"Center Name: {center['name']}\n\n"
                    f"Minimum Age: {session['min_age_limit']}\n"
                    f"Dose 1: {session['available_capacity_dose1']}, "
                    f"Dose 2: {session['available_capacity_dose2']}\n"
                    f"Fee type: {center['fee_type']}\n\n"
                    f"#cowin #vaccine #Aurangabad"
                )
                try:
                    # api.update_status(message) # Commented out for safety
                    print(f"Update found for {center['name']}")
                except Exception as e:
                    print(f"Twitter Error: {e}")

if __name__ == "__main__":
    print("Bot started...")
    schedule.every(10).seconds.do(lambda: fetch_data_for_state(mh_district_ids))
    
    while True:
        schedule.run_pending()
        time.sleep(1)
