import requests
import os

class DataManager:
    def __init__(self):
        self.endpoint = "https://api.sheety.co/3bba0cae9ad175734f51ce918374111d/flightDeals/prices"
        self.token = os.environ("SHEETY_TOKEN")
        self.auth = {
            "Authorization": f"Bearer {self.token}"
        }
        self.data = {}
        self.get_data()

    def get_data(self):
        # response = requests.get(url=self.endpoint, headers=self.auth)
        response = requests.get(url=self.endpoint)
        data = response.json()
        self.data = data['prices']
        return self.data

    def update_destination_code(self, code, row_id):
        update_data = {
            "price": {
                "iataCode": code
            }
        }
        response = requests.put(url=f"{self.endpoint}/{row_id}", json=update_data)

