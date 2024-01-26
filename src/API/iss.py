import smtplib
import time
from datetime import datetime

import requests

my_lat = 22.718670
my_lng = 75.855713
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])

    if my_lat-5 <= iss_latitude <= my_lat+5 and my_lng-5 <= iss_longitude <= my_lng+5:
        return True


def is_night():
    parameters = {
        "lat": my_lat,
        "lng": my_lng,
        "formatted":0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        my_email = "example@gmail.com" # replace it with you actual email
        password = "password" # replace it with your actual password
        with smtplib.SMTP('email sender SMTP.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="vikasgole089@gmail.com",
                                msg="subject: ISS Updates\n\n Iss is over your head.")


