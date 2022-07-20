import os
import requests
from send_sms import Sms


class GetNews():

    def __init__(self):
        self.COMPANY_NAME = os.environ.get("COMPANY_NAME")
        self.NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
        self.API_KEY = os.environ.get("NEWS_API_KEY")
        self.news_params = {
            "apiKey": self.API_KEY,
            "qInTitle": self.COMPANY_NAME,
            "pageSize": 5,
        }
        self.response = requests.get(url=self.NEWS_ENDPOINT,
                                     params=self.news_params)
        self.response.raise_for_status()
        self.data = self.response.json()
        self.data = self.data["articles"][0:3]

    def get_articles(self):
        self.message = [
            f"{self.COMPANY_NAME}\n Headline: {article['title']}.\nBrief: {article['description']}" for article in self.data]

        for article in self.message:
            Sms().send_sms(message=article)
