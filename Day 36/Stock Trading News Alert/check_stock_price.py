import os
import requests


class CheckStockPrice:

    def __init__(self):
        STOCK_NAME = os.environ.get("STOCK_NAME")
        self.stock_params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": STOCK_NAME,
            "apikey": os.environ.get("STOCK_API_KEY")
        }
        self.STOCK_ENDPOINT = "https://www.alphavantage.co/query"

    def check_price(self):
        response = requests.get(url=self.STOCK_ENDPOINT,
                                params=self.stock_params)
        response.raise_for_status()
        data = response.json()["Time Series (Daily)"]
        dates = list(data)

        last_close = dates[0]
        self.last_close_price = float(data[last_close]["4. close"])

        prior_close = dates[1]
        self.prior_close_price = float(data[prior_close]["4. close"])

        abs_value_change = abs(self.last_close_price - self.prior_close_price)

        self.percentage_change = (
            abs_value_change / self.prior_close_price) * 100
        if self.percentage_change > 5:
            return True
        else:
            return False
