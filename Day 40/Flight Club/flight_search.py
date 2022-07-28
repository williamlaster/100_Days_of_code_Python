import requests
from flight_data import FlightData
import os
from pprint import pprint


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    pass

    def __init__(self):
        self.SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
        self.TEQUILA_ENDPOINT = os.environ.get("TEQUILA_ENDPOINT")
        self.TEQUILA_HEADER = {
            "apikey": os.environ.get("TEQUILA_API_KEY")
        }

    def update_sheet(self, id, data):
        city = data["price"]["city"]
        data["price"]["iataCode"] = self.search_iata(city=city)
        response = requests.put(url=f"{self.SHEETY_ENDPOINT}{id}", json=data)
        response.raise_for_status()

    def search_iata(self, city):
        search_params = {
            "term": city,
            "locale": "en-US",
            "location_types": "airport",
            "active_only": "true"
        }
        response = requests.get(
            self.TEQUILA_ENDPOINT, params=search_params, headers=self.TEQUILA_HEADER)
        response.raise_for_status()
        iata_code = response.json()["locations"][0]["id"]
        return iata_code

    def get_flights(self, flyfrom, flyto, from_time, to_time):
        SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
        self.search_params = {
            "fly_from": flyfrom,
            "fly_to": flyto,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "adults": 1,
            "curr": "USD",
            "locale": "en",

        }
        response = requests.get(url=SEARCH_ENDPOINT,
                                params=self.search_params, headers=self.TEQUILA_HEADER)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            try:
                self.search_params["max_stopovers"] = 1
                response = requests.get(
                    url=SEARCH_ENDPOINT,
                    headers=self.TEQUILA_HEADER,
                    params=self.search_params,
                )
                data = response.json()["data"][0]
                pprint(data)
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[
                        0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                return flight_data
            except IndexError:
                print(f"No flights found for {flyto}.")
                return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data
