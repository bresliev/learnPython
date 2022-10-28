import requests


class FlightData:
    # This class is responsible for structuring the flight data.
    TEQUILA_API_KEY = "OCXjQhhspPHmmB-9u_iTAF8XHst1Llyb"
    TEQUILA_URL = "https://api.tequila.kiwi.com/v2/search"
    AMADEUS_API_KEY = "WCHpAZy4l2BC6ZlEAqlm5oBnd0r4sD9V"
    AMADEUS_SECRET = "HTV3aUFXXAYExvi0"
    AMADEUS_IATA_URL = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
    DEPARTURE_DESTINATION = "BEG"

    TEQUILA_HEADERS = {
        "apikey": TEQUILA_API_KEY
    }
    amadeus_headers = {
        "Authorization": "Bearer m9OB64jlGpnMUVzNGomxamz9PZiv"
    }
    AMADEUS_TOKEN_HEADERS = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    def __init__(self):

        self.tequila_params = {
            "fly_from": "LGA",
            "fly_to": "MIA",
            "dateFrom": "01/11/2022",
            "dateTo": "03/11/2022"
        }

        self.amadeus_params = {
            "keyword": "",
        }

        self.amadeus_token_params = {
            "grant_type": "client_credentials",
            "client_id": self.AMADEUS_API_KEY,
            "client_secret": self.AMADEUS_SECRET
        }

        self.token = self.get_amadeus_token()

        self.amadeus_headers = {
            "Authorization": "Bearer " + self.token["access_token"]
        }



    def get_prices(self):
        response = requests.get(self.TEQUILA_URL, params=self.tequila_params, headers=self.TEQUILA_HEADERS)
        data = response.json()
        return data

    def get_iata(self, destination):
        response = requests.get(self.AMADEUS_IATA_URL, params=self.amadeus_params, headers=self.amadeus_headers)
        data = response.json()
        return data

    def get_amadeus_token(self):
        response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token",
                                 headers=self.AMADEUS_TOKEN_HEADERS, data=self.amadeus_token_params)
        return response.json()
