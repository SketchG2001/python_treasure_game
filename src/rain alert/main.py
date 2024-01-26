import os

import requests
from twilio.rest import Client

account_sid = os.environ.get('sms_account_id')
auth_token = os.environ.get('sms_account_auth_code')
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get('weather_api')

weather_params = {
    "lat": 2.105108,
    "lon": 99.827843,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        # print(hour_data["weather"][0]["id"])
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Hey there! ☔️ Looks like rain is expected today."
             " Don't forget to bring your umbrella when you head out!",
        from_='+12406541551',
        to='+919584363361'
    )
    print(message.status)

