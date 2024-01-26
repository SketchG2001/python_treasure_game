import os
import requests
from twilio.rest import Client

auth_code = os.environ.get('auth_code')
sms_s_id = os.environ.get('sms_account_id')

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "H125AN7S9TOOOT4B"
NEWS_API_KEY = "91e02342841644a992a0b6b9e92cd92d"


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]

# yesterday's closing stock price
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
print(yesterday_closing_price)

# Get the day before yesterday's closing stock price
day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday["4. close"])
print(day_before_yesterday_closing_price)

# Find the positive difference between yesterday and the day before yesterday.
difference = yesterday_closing_price - day_before_yesterday_closing_price
# print(difference)
# up_down = None
# if difference > 0:
#     up_down = "🔺"
# else:
#     down_down = "🔻"

# Work out the percentage difference in price between yesterday and the day before yesterday.
diff_percent = (difference / yesterday_closing_price) * 100
# print(diff_percent)

# If the percentage difference is greater than 5 then get news.
if diff_percent > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qIntitle": COMPANY_NAME
    }

    # Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    # Use Python slice operator to create a list that contains the first 3 articles. Hint:
    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [f"Headline: {article['title']}. \n Brief: {article['description']}." for article in three_articles]
    client = Client(sms_s_id, auth_code)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+12406541551',
            to='+919584363361'
        )
        print(message.status)
