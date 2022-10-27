import requests
from pprint import pprint

# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.url = "https://api.sheety.co/3cd8d5bfbdaceb99e8a938407728788c/flightDeals/prices"

    def get(self):
        response = requests.get(url=self.url, verify=False)
        response.raise_for_status()
        return response.json()["prices"]

