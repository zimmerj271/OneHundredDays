import requests
from datetime import datetime
import smtplib
import urllib3
# The following is needed to bypass HTTPS insecure request warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

MY_LAT = 43.389180 # Your latitude
MY_LONG = -115.981850 # Your longitude
MY_EMAIL = "vikingsmash@yahoo.com"
MY_PASSWORD = "qgyxtfldhrwczwiw"
SMTP_SERVER = "smtp.mail.yahoo.com"



# Your position is within +5 or -5 degrees of the ISS position.
def iss_nearby():
    global MY_LAT
    global MY_LONG

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5:
        return True
    else:
        return False

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.utcnow()  # Get current time in UTC

    if sunset <= time_now.hour < sunrise:
        return True
    else:
        return False


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.  Instructor uses a while loop.  Cron is a better solution.

if iss_nearby() and is_night():
    message = f"Subject:Look Up!☝\n\nThe ISS is above."
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="zimmerj271@pm.me", msg=message)
