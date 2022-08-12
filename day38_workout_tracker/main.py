import requests
from datetime import datetime
import os

# Nutritionix API credentials
NX_APP_ID = 'c9a45a95'
NX_APP_KEY = '344d271b45b0ad2846119c15072456f6'
# Nutritionix API query parameters
gender = "male"
weight = "83.9"  # weight in kg
height = "175.3"  # height in cm
age = "42"

# API Endpoint URLs
NX_EXERCISE_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_ENDPOINT = 'https://api.sheety.co/3bba0cae9ad175734f51ce918374111d/myWorkouts/workouts'

# query = input("What exercises have you done? ")
query = "I performed 100 push-ups, 200 jumping jacks, and I ran 10 km."

nx_headers = {
    "x-app-id": NX_APP_ID,
    "x-app-key": NX_APP_KEY,
}
nx_parameters = {
    "query": query,
    "gender": gender,
    "weight_kg": weight,
    "height_cm": height,
    "age": age
}
response = requests.post(url=NX_EXERCISE_ENDPOINT, json=nx_parameters, headers=nx_headers)
print(response.raise_for_status())
exercises = response.json()["exercises"]
# print(response.json())
# with open("exercise.json", "w") as file:
#     json.dump(response.json(), file)

sheety_headers = {
    "Date": "21/07/2020",
    "Time": "15:00:00",
    "Exercise": "Running",
    "Duration": "22",
    "Calories": "130"
}
now = datetime.now()
today = now.strftime("%d/%m/%Y")
time = now.strftime("%X")
# No authentication
# for action in exercises:
#     act = {
#         "workout": {
#             "date": today,
#             "time": time,
#             "exercise": action["name"].title(),
#             "duration": action["duration_min"],
#             "calories": action["nf_calories"]
#         }
#     }
#     sheety_response = requests.post(url=SHEETY_ENDPOINT, json=act)
#     print(sheety_response.status_code)

# Basic authentication
# sheety_auth = ("username", "password")
# for action in exercises:
#     act = {
#         "workout": {
#             "date": today,
#             "time": time,
#             "exercise": action["name"].title(),
#             "duration": action["duration_min"],
#             "calories": action["nf_calories"]
#         }
#     }
#     sheety_response = requests.post(url=SHEETY_ENDPOINT, json=act, auth=sheety_auth)
#     print(sheety_response.status_code)

# Bearer/Token authentication
SHEETY_TOKEN = os.environ("SHEETY_TOKEN")
sheety_auth = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}
for action in exercises:
    act = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": action["name"].title(),
            "duration": action["duration_min"],
            "calories": action["nf_calories"]
        }
    }
    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=act, headers=sheety_auth)
    print(sheety_response.status_code)