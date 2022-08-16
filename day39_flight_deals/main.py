#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

ORIGIN_CITY = "BOI"

data_manager = DataManager()
flight_search = FlightSearch()
sms_manager = NotificationManager()
sheet_data = data_manager.data

# Check for missing destination codes and update if missing
update_data = False
for row in sheet_data:
    if not row['iataCode']:
        update_data = True
        code = flight_search.get_destination_code(row['city'])
        data_manager.update_destination_code(code=code, row_id=row['id'])

if update_data:
    sheet_data = data_manager.get_data()

for row in sheet_data:
    raw_flight_data = flight_search.flight_search(fly_to=row['iataCode'], fly_from=ORIGIN_CITY)
    flight_data = FlightData(raw_flight_data)
    # check if price meets threshold
    if flight_data.price < row['lowestPrice']:
        message = f"\nRound trip to {row['city']} for ${flight_data.price}\n{flight_data.trip_message('depart')}" \
                  f"\n{flight_data.trip_message()}"
        sms_manager.send_message(message)

