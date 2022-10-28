# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import data_manager as dm
from pprint import pprint
import flight_data as fd
from datetime import datetime, timedelta

data_mngr = dm.DataManager()


# flight_data = fd.FlightData()


def intialize_prices():
    flight_data = fd.FlightData()
    #    token = flight_data.get_amadeus_token()
    #     flight_data.amadeus_headers["Authorization"] = "Bearer "+token["access_token"]
    data_iata = data_mngr.intialize_prices(flight_data)


#
#
#     print(flight_data.amadeus_headers)
#     pprint(token)
#     pprint(data_iata)

#
# def deals():
#     for destionation in destinations:
#         dateFrom = input("Enter date from (dd/mm/yyyy):")
#         dateTo = input("Enter date to (dd/mm/yyyy):")
#
#         dateFrom = str(datetime.now().replace(day=1) + timedelta(days_in_month(dateFrom)))
#         flight_data = fd.FlightData()
#         data_flight = flight_data.get_prices()
#         pprint(data_flight)


intialize_prices()
