import requests
import datetime as dt

LATITUDE = 43.389180
LONGITUDE = -115.981850

# response = requests.get(url="http://api.open-notify.org/iss-now.json") # response from API
# response.raise_for_status()
# data = response.json()
# longitude = float(data["iss_position"]["longitude"])
# latitude = float(data["iss_position"]["latitude"])
# iss_position = (longitude, latitude)
# print(iss_position)

# HTTP Status Codes: https://www.webfx.com/web-development/glossary/http-status-codes/

api_parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0
}

# The following is needed to bypass HTTPS insecure request warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# verify=False to bypass SSL certification check
response = requests.get("https://api.sunrise-sunset.org/json", params=api_parameters, verify=False)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")
sunset = data["results"]["sunset"].split("T")
sunrise_hour = sunrise[1].split(":")[0]
sunset_hour = sunset[1].split(":")[0]

current_time = dt.datetime.now()

print(sunrise_hour, sunset_hour, current_time)