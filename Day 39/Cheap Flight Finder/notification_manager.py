import os
from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    pass

    def __init__(self):
        self.account_sid = os.environ.get("TWILIO_SID")
        self.auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

    def send_sms(self, message):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(
                body=message,
                from_=os.environ.get("FROM_PHONE_NUMBER"),
                to=os.environ.get("TO_PHONE_NUMBER")
            )
        print(message.status)
