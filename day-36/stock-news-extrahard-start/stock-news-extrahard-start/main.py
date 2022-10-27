import requests
from datetime import datetime
import time
from datetime import timedelta
import smtplib

MY_PASSWORD = "ycngyrakpjgbhsxa"
MY_FROM_EMAIL = "nikola.pythonista@gmail.com"
MY_TO_EMAIL = "nikola.bresliev@gmail.com"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
#Alpha advantage
STOCK_PRICE_API_KEY = "C1B61X6NCJIMDGY9"
stock_api_params={
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": STOCK_PRICE_API_KEY
    }

STOCK_URL = "https://www.alphavantage.co/query"

#https://newsapi.org/v2/everything?q=tesla&from=2022-09-26&sortBy=publishedAt&apiKey=7a7e6261ed874ac593db582bd55877af
#News
NEWS_API_KEY = "7a7e6261ed874ac593db582bd55877af"

NEWS_URL = "https://newsapi.org/v2/everything"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_response = requests.get(STOCK_URL, params=stock_api_params)
stock_data = stock_response.json()
time_series = stock_data["Time Series (60min)"]
last_close_key = next(iter(time_series))
last_close = time_series[last_close_key]
last_close_time = datetime.strptime(last_close_key, "%Y-%m-%d %H:%M:%S")

previous_close_key = last_close_time - timedelta(days=1)
previous_close = time_series[str(previous_close_key)]

delta = (float(last_close["4. close"])-float(previous_close["4. close"]))/float(last_close["4. close"])*100
if delta > 3 or delta < -3:
    print("yu need a news")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_api_parameters = {
    "q": "tesla",
    "from": str(last_close_time - timedelta(days=30)),
    "sortBy": "publishedAt",
    "apiKey": NEWS_API_KEY
}

news_response = requests.get(NEWS_URL, params=news_api_parameters)
news_data = news_response.json()
first_three_news = news_data["articles"][:3]

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=MY_FROM_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_FROM_EMAIL, to_addrs=MY_TO_EMAIL,
                        msg="Subject: difference\n" + str(delta))
    for item in first_three_news:
        msg = "Subject: "+item["title"]+"\n"+item["title"]
        connection.sendmail(from_addr=MY_FROM_EMAIL, to_addrs=MY_TO_EMAIL,
                            msg=msg.encode('utf-8'))

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

