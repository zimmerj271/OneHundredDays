import requests
from twilio.rest import Client
# import json

OWM_endpoint = "http://api.openweathermap.org/data/2.5/onecall"
OWM_API_KEY = os.environ.get("OWM_API_KEY")
TWILIO_ACC_SID = os.environ.get("TWILIO_ACC_SID")
TWILIO_AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 43.389180,
    "lon": -115.981850,
    "appid": OWM_API_KEY,
    "units": "imperial",
    "exclude": "current,minutely,daily"
}

# Get weather data
response = requests.get(url=OWM_endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
# Save weather data to json file
# with open("weather.json", 'w') as file:
#     json.dump(data, file)

# Open saved weather data from json file
# with open("weather.json", 'r') as file:
#     data = json.load(file)


will_rain_today = False
weather_slice = data['hourly'][:12]
for hour in weather_slice:
    condition_code = hour['weather'][0]['id']
    if condition_code < 700:
        will_rain_today = True

if will_rain_today:
    twilio_client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)
    message = twilio_client.messages.create(
        body="It's going to rain today.  Remember to bring an ☂️",
        from_="+12166775599",
        to="+12087809669"
    )
    print(message.status)
