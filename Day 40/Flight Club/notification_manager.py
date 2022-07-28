import os
from twilio.rest import Client
import smtplib


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

    def send_emails(self, email, message, link=""):
        FROM_EMAIL = os.environ.get("FROM_EMAIL")
        EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=FROM_EMAIL, password=EMAIL_PASSWORD)
            for to in email:
                connection.sendmail(
                    from_addr=FROM_EMAIL,
                    to_addrs=to,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{link}".encode(
                        'utf-8')
                )
