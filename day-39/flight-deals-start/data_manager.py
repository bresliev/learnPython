import requests
from pprint import pprint

# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.url = "https://api.sheety.co/3cd8d5bfbdaceb99e8a938407728788c/flightDeals/prices"
        self.destinations = self.get()

    def get(self):
        response = requests.get(url=self.url, verify=False)
        response.raise_for_status()
        return response.json()["prices"]

    def intialize_prices(self, flight_data):

        for destination in self.destinations:
            flight_data.amadeus_params["keyword"] = destination["city"].upper()
            data_iata = flight_data.get_iata(destination=destination)

            for item in data_iata:
                print(item)
                if item == "data":
                    print(type(data_iata[item][0]))
                    print(data_iata[item][0]["subType"])
                    print(data_iata[item][0]["name"])
                    print(data_iata[item][0]["address"]["countryCode"])
                    print(data_iata[item][0]["iataCode"])

        https://api.sheety.co/3cd8d5bfbdaceb99e8a938407728788c/flightDeals/prices/[Object ID]

        response = requests.put(url=put_value_endpoint, json=put_value_params, headers=headers)
                # if item == "data":# and data_iata[item]["subType"] == "city":
                #
                #     for itt in data_iata[item]:
                #         if itt["subType"] == "city":
                #             print(itt["subType"])
                #             print(itt["name"])
                #             print(itt["address"]["countryCode"])
                #             print(itt["iataCode"])
                #             # destination_price = {"city": destination["city"],
                #             #                      "iataCode": item["iataCode"] for item in data_iata if item["city"] == destination["city"] and item["subType"] == "city",
                #             #                       "lowestPrice": 1000}
                #
                #


# [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2},
#  {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3},
#  {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4},
#  {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5},
#  {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6},
#  {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7},
#  {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8},
#  {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9},
#  {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]

# City	IATA Code	Lowest Price
# Paris		54
# Berlin		42
# Tokyo		485
# Sydney		551
# Istanbul		95
# Kuala Lumpur		414
# New York		240
# San Francisco		260
# Cape Town		378
