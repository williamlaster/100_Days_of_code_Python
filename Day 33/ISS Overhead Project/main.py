import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 36.157450  # Your latitude
MY_LONG = -97.087293  # Your longitude

EMAIL = "YOUR EMAIL HERE"
PASSWORD = "YOUR PASSWORD HERE"
iss_lat = 0
iss_long = 0


def in_range():
    global iss_lat, iss_long
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_lat = iss_latitude
    iss_long = iss_longitude

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - iss_latitude <= 5 and MY_LAT - iss_latitude >= -5:
        if MY_LONG - iss_longitude <= 5 and MY_LONG - iss_longitude >= -5:
            return True


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour < sunrise:
        return True


# If the ISS is close to my current position
# and it is currently dark send an email.
# run the code every 60 seconds.
while in_range() and is_dark():
    time.sleep(60)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:ISS is Overhead\n\nThe ISS is currently overhead!\nAt lat:{iss_lat} long:{iss_long}\n\n  - This is an automated email"
        )
