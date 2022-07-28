import requests
import os


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
        self.USER_ENDPOINT = os.environ.get("SHEETY_USER_ENDPOINT")
        self.SHEETY_ID = os.environ.get("SHEETY_ID")
        self.SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
        self.sheety_headers = {
            "Authorization": f"{self.SHEETY_ID} {self.SHEETY_TOKEN}"}

    def get_sheet_data(self):
        SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
        sheety_headers = {
            "Authorization": f"{self.SHEETY_ID} {self.SHEETY_TOKEN}"}
        response = requests.get(url=SHEETY_ENDPOINT,
                                headers=sheety_headers)
        print(response.text)
        data = response.json()
        return data["prices"]

    def add_user(self):
        self.first_name = input("What is your first name?\n").title()
        self.last_name = input("What is your last name?\n").title()
        self.email = input("What is your email?\n").lower()
        self.email_check = input("Please confirm your email.\n").lower()

        if self.email == self.email_check:
            user = {
                "user": {
                    "firstName": self.first_name,
                    "lastName": self.last_name,
                    "email": self.email

                }
            }
            response = requests.post(
                url=self.USER_ENDPOINT, json=user, headers=self.sheety_headers)
            response.status_code
            response.raise_for_status()
            if response.status_code == 200:
                print("You're in the club!")
        else:
            print("Email address did not match, please try again.")
            self.add_user()

    def get_emails(self):
        response = requests.get(url=self.USER_ENDPOINT,
                                headers=self.sheety_headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
