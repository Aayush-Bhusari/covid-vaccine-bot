covid-vaccine-bot
(Archival - July 2021) Python bot for monitoring vaccine availability via CoWin and Twitter APIs.

CoWin Twitter Vaccine Notifier Bot

## Project Overview
This project implements an automated monitoring system designed to bridge the gap between vaccine availability and public awareness during the 2021 COVID-19 pandemic. By integrating the CoWin Public API with the Twitter API, the bot performs high-frequency polling of district-specific vaccination centers to identify available inventory for Dose 1 and Dose 2. When a center reports a positive capacity, the script parses the JSON response, formats a structured alert containing the center name, pincode, and age requirements, and publishes it via a Twitter status update. This real-time notification loop was intended to assist users in securing appointments in competitive regions like Aurangabad by reducing the latency between slot release and public discovery.

Technical Stack
* Language: Python 3
* APIs: CoWin Public API, Twitter (v1.1/v2 via Tweepy)
* Libraries: Tweepy, Requests, Schedule, Python-Dotenv

Setup and Installation
1. Clone the repository to your local machine.
2. Install the required dependencies using the command: pip install -r requirements.txt.
3. Create a file named .env in the root directory.
4. Populate the .env file with your Twitter API credentials (CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET).
5. Execute the script using: python main.py.

## Disclaimer
This repository is maintained for archival and portfolio purposes to demonstrate API integration and automation workflows used during the 2021 vaccine rollout in India.
