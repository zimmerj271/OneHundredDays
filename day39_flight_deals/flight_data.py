from datetime import datetime


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, data):
        self.data = data
        self.price = self.data['price']
        self.city_to = self.data['cityTo']
        self.city_from = self.data['cityFrom']

    def trip_info(self, trip):
        trip_data = self.data['route'][trip]
        trip_info = {
            "flight_no": trip_data["flight_no"],
            "carrier": trip_data["operating_carrier"],
            "departure_city": trip_data['cityFrom'],
            "departure_airport_code": trip_data['cityCodeFrom'],
            "arrival_city": trip_data['cityTo'],
            "arrival_airport_code": trip_data['cityCodeTo'],
            "departure_time": datetime.strptime(trip_data['local_departure'], "%Y-%m-%dT%H:%M:%S.000Z"),
            "arrival_time": datetime.strptime(trip_data['local_arrival'], "%Y-%m-%dT%H:%M:%S.000Z")
        }
        return trip_info

    def trip_message(self, message_type="return"):
        # data = {}
        # travel_type = ""
        if message_type == "depart":
            data = self.trip_info(0)
            travel_type = "leaving"
        else:
            data = self.trip_info(1)
            travel_type = "returning back"
        date = data["departure_time"].strftime("%m/%d/%Y")
        time = data["departure_time"].strftime("%H:%M")
        return f"Flight {data['carrier']} {data['flight_no']} to {data['arrival_city']} {travel_type} {date} at {time}"
