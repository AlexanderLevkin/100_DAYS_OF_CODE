import os

import requests
import datetime as dt
from twilio.rest import Client

account_sid = "AC7aafaa494a04c277a700ffbdcae8a8f5"
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_KEY_STOCK = "X3960ACWF1PW668Z"
API_KEY_NEWS = "a6cc9246f8974e52b00ed97e56ad1df0"

yesterday_data = (dt.datetime.now() - dt.timedelta(days=2)).strftime('%Y-%m-%d')
day_before_yesterday_data = (dt.datetime.now() - dt.timedelta(days=3)).strftime('%Y-%m-%d')

params_of_news = {
    "apiKey": API_KEY_NEWS,
    "q": STOCK,
    "from": yesterday_data,
    "to": day_before_yesterday_data
}

params_of_stock = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": API_KEY_STOCK
}

response_of_stock = requests.get(url=STOCK_ENDPOINT, params=params_of_stock)
data_of_stock = response_of_stock.json()
yesterday_value = int(data_of_stock['Time Series (Daily)'][yesterday_data]['6. volume'])
day_before_yesterday_value = int(data_of_stock['Time Series (Daily)'][day_before_yesterday_data]['6. volume'])
percent_between_days = round((yesterday_value - day_before_yesterday_value) / day_before_yesterday_value * 100)

response_of_news = requests.get(url=NEWS_ENDPOINT, params=params_of_news)
data_of_news = response_of_news.json()

news = data_of_news['articles'][:3]

client = Client(account_sid, auth_token)
message = client.messages.create(
    body=('\n'.join([f"TSLA: {'🔺' if percent_between_days > 5 else '🔻'}{percent_between_days}%\nHeadline"
                     f":{news[i]['title']}\nBrief:{news[i]['description']}"
                     if percent_between_days > 5 or percent_between_days <= 5
                     else "Wrong response"
                     for i in range(0, 3)])),
    from_="+15077040526",
    to="+375333371531"
)
print(message.status)