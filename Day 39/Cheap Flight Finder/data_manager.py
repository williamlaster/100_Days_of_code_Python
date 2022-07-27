import requests
import os


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
        self.header = {
            "Authorization": os.environ.get("SHEETY_TOKEN")
        }

    def get_sheet_data(self):
        response = requests.get(url=self.SHEETY_ENDPOINT, headers=self.header)
        response.raise_for_status()
        data = response.json()
        return data["prices"]
