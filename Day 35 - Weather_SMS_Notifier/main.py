# Weather API program to send SMS on phone when it is going to rain in your town
# So you will never forget to take an umbrella
# Requipments: OpenWeather API account and Twillio account
import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from dotenv import load_dotenv

load_dotenv()

WEATHER_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'
API_KEY = os.getenv('API_KEY')
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
tw_number = os.getenv('TWILIO_TRIAL_NUMBER')
tel = os.getenv('TEL') # Your phone number

weather_params = {
    "lat": 41.715137,
    "lon": 44.827095,
    "exclude": 'current,minutely,daily',
    "appid": API_KEY
}

response = requests.get(WEATHER_ENDPOINT, params=weather_params)
response.raise_for_status()
data = response.json()
weather_data = data["hourly"][:12]

for hour in weather_data:
    condtion = hour["weather"][0]["id"]
    if int(condtion) < 700:
        rain = True
        
if rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = { "https": os.environ["https_proxy"]}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    msg = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☂️",
            from_=tw_number, 
            to=tel 
        )
    print(msg.status)