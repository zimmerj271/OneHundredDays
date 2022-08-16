import requests
import os
from datetime import date, timedelta


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = os.environ("TEQUILA_KEY")
        self.headers = {
            "apikey": self.api_key
        }
        self.endpoint = 'https://tequila-api.kiwi.com'

    def get_destination_code(self, city):
        location_endpoint = f"{self.endpoint}/locations/query"
        query = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(url=location_endpoint, headers=self.headers, params=query)
        data = response.json()
        return data['locations'][0]['code']

    def flight_search(self, fly_to, fly_from):
        global API_KEY
        global ENDPOINT
        search_endpoint = f"{self.endpoint}/v2/search"
        begin_date = date.today()
        end_date = begin_date + timedelta(weeks=26)
        query = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "dateFrom": begin_date.strftime('%d/%m/%Y'),
            "dateTo": end_date.strftime('%d/%m/%Y'),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "partner_market": "us",
            "curr": "USD",
        }
        response = requests.get(url=search_endpoint, params=query, headers=self.headers)
        try:
            data = response.json()["data"][0]
            return data
        except IndexError:
            print(f"No flights found for {fly_to}")
            return None

