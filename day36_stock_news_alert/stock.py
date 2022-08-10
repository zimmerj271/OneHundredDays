import os
import requests
from datetime import date, timedelta
from twilio.rest import Client
import json

TICKER = "TSLA"
COMPANY_NAME = "Tesla"
# COMPANY_NAME = "Trump"
# COMPANY_NAME = "Micron%20Technology"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

AV_API_KEY = os.environ.get("AV_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_ACC_SID = os.environ.get("TWILIO_ACC_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

av_endpoint = "https://www.alphavantage.co/query"
av_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": TICKER,
    "apikey": AV_API_KEY
}
news_endpoint = "https://newsapi.org/v2/everything"
news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

# Get stock price action from API
av_response = requests.get(url=av_endpoint, params=av_params)
av_response.raise_for_status()
data = av_response.json()

# Get yesterday's open and close stock price and calcualte % change
yesterday = date.today() - timedelta(days=1)
price_action = data["Time Series (Daily)"]
open_price = float(price_action[f"{yesterday.strftime('%Y-%m-%d')}"]["1. open"])
close_price = float(price_action[f"{yesterday.strftime('%Y-%m-%d')}"]["4. close"])
percent_change = round((close_price - open_price) / open_price * 100, 2)

if abs(percent_change) > 5:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    if percent_change > 0:
        header = f"\n{TICKER}: 🔺{percent_change}%\n"
    else:
        header = f"\n{TICKER}: 🔻{percent_change}%\n"

    news_response = requests.get(url=news_endpoint, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()

    news_articles = news_data["articles"]
    if len(news_articles) < 3:
        number_of_articles = len(news_articles)
    else:
        number_of_articles = 3

    text_list = [f"Headline: {article['title']}\nBrief: {article['description']}" for
                 article in news_articles[:number_of_articles]]
    text = header + "\n\n".join(text_list)

    ## STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    twilio_client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)
    message = twilio_client.messages.create(
        body=text,
        from_="+12166775599",
        to="+12087809669"
    )
    print(message.status)

#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

