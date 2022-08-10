import requests
from datetime import datetime, timedelta
import json

# STOCK = "TSLA"
# COMPANY_NAME = "Tesla Inc"
TICKER = "BTC"
CRYPTO_CURRENCY = "Bitcoin"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
AV_endpoint = "https://www.alphavantage.co/query"
AV_API_KEY = "03XW38MVAFZHGM15"
av_params = {
    "function": "CRYPTO_INTRADAY",
    "symbol": TICKER,
    "market": "USD",
    "interval": "60min",
    "apikey": AV_API_KEY
}
# av_response = requests.get(url=AV_endpoint, params=av_params)
# av_response.raise_for_status()
# data = av_response.json()
# with open("stock.json", "w") as file:
#     json.dump(data, file)
with open("stock.json", "r") as file:
    data = json.load(file)

market_open = "09:00:00" # EST
market_close = "16:00:00" # EST

delta = timedelta(hours=14)
today = datetime.utcnow() - timedelta(hours=2)
yesterday = datetime.today() - delta
# print(today, yesterday)
price_action = data["Time Series Crypto (60min)"]
# print(today.strftime("%Y-%m-%d"), today.hour)
open_price = float(price_action[f"{today.strftime('%Y-%m-%d')} {today.hour}:00:00"]["1. open"])
close_price = float(price_action[f"{yesterday.strftime('%Y-%m-%d')} {yesterday.hour}:00:00"]["4. close"])
percent_change = (open_price - close_price) / close_price * 100
if abs(percent_change) > 5:
    print("Get news")
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


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

