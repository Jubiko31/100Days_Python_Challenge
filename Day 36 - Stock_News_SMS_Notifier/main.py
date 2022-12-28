# Stock Exchange & News SMS notifier with API
import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_ACCESS_SID = os.getenv('TWILIO_ACCESS_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')
TEL = os.getenv('TEL')

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": os.getenv('ALPHAV_STOCK_API_KEY'),
}

response = requests.get(STOCK_ENDPOINT,params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
prev_data = data_list[0]   # yesterday data
prev_closing_price = prev_data["4. close"]

day_before = data_list[1]  # the day before yesterday data
day_before_closing_price = day_before["4. close"]

diff = float(prev_closing_price) - float(day_before_closing_price)
up_down = None
if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_prct = round(diff / float(prev_closing_price)) * 100
if abs(diff_prct) > 1:
    news_params = {
        "apiKey": os.getenv('NEWS_API_KEY'),
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    new_articles = news_response.json()["articles"]
    
    articles = new_articles[:3]
    
    pretter_articles = [f"Headline: {article['title']}/ \nBrief: {article['description']}" for article in articles]

    client = Client(TWILIO_ACCESS_SID, TWILIO_AUTH_TOKEN)
    for article in pretter_articles:
        msg = client.messages.create(
            body=article,
            from_=TWILIO_NUMBER,
            to=TEL
        )