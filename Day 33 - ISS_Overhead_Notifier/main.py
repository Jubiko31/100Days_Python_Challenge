# Program notifies when ISS is right above your sky
# And sends email to loop up.
# While code is running on background notifier is executed every 60secs
import requests
import smtplib
from datetime import datetime
from time import sleep

API = "http://api.open-notify.org/iss-now.json"
SUNSET_API = "https://api.sunrise-sunset.org/json"
MY_EMAIL = "<email>"
MY_PASSWORD = "<password>"
MY_LAT = 41.693630
MY_LONG = 44.801620

def is_iss_overhead():
    response = requests.get(url=API)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_night_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(SUNSET_API, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    sleep(60)
    if is_iss_overhead() and is_night_time():
        conn = smtplib.SMTP("smtp.gmail.com")
        conn.starttls()
        conn.login(MY_EMAIL, MY_PASSWORD)
        conn.sendmail(
            from_addr=MY_EMAIL,
            to_addr=MY_EMAIL,
            msg="Subject:Look up!\n\nThe ISS is currently above you in the sky!"
        )
        conn.close()