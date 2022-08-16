from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/3bba0cae9ad175734f51ce918374111d/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/3bba0cae9ad175734f51ce918374111d/flightDeals/users"


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.user_data = {}
        self.get_user_data()

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def add_user(self, first, last, email):
        new_data = {
            "user": {
                "firstName": first,
                "lastName": last,
                "email": email
            }
        }
        response = requests.post(url=SHEETY_USERS_ENDPOINT, json=new_data)
        print(response.text)

    def get_user_data(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT)
        data = response.json()
        self.user_data = data["users"]
        return self.user_data

    def get_user_email(self):
        return [row["Email"] for row in self.user_data]
