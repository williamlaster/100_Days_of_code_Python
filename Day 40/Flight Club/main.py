import datetime
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
now = datetime.datetime.now()
TOMORROW = now + datetime.timedelta(days=1)
DATE_TO = now + datetime.timedelta(days=181)
FLY_FROM = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_sheet_data()
send_message = NotificationManager()


for row in sheet_data:
    if row["iataCode"] == '':
        data = {"price": row}
        flight_search.update_sheet(id=str(row["id"]), data=data)

for destination in sheet_data:
    flight = flight_search.get_flights(
        flyfrom=FLY_FROM,
        flyto=destination["iataCode"],
        from_time=TOMORROW,
        to_time=DATE_TO
    )

    try:
        if flight.price < destination["lowestPrice"]:
            users = data_manager.get_emails()
            emails = [row["email"] for row in users]
            names = [row["firstName"] for row in users]

            message = f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            if flight.stop_overs > 0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            link = f"https://www.google.com/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

    except AttributeError:
        continue

    send_message.send_emails(email=emails, message=message, link=link)
