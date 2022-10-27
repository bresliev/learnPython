# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import data_manager
from pprint import pprint

data_mngr = data_manager.DataManager()
pprint(data_mngr.get())
