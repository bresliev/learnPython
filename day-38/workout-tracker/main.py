from datetime import datetime

import requests

APP_ID = "3178cd07"
API_KEY = "6865be22363a0659e5747c6c8a979a32"
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
USER_ID = "nikolabresliev"
GENDER = "Male"
WEIGHT_KG = 93
HEIGHT_CM = 173
AGE = 52

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_text = "running 4 hours 20221027"

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(EXERCISE_ENDPOINT, json=parameters, headers=headers)
exercise = response.json()["exercises"][0]["user_input"]
duration = response.json()["exercises"][0]["duration_min"]
calories = response.json()["exercises"][0]["nf_calories"]

SHEETY_URL = "https://api.sheety.co/3cd8d5bfbdaceb99e8a938407728788c/nikiPyWorkouts/workouts"
resp = requests.get(SHEETY_URL, verify=False)
print(f"evo ga ide sada {resp.headers}")
data = resp.json()
print(data)
# for exercise in result["exercises"]:
#     sheet_inputs = {
#         "workout": {
#             "date": today_date,
#             "time": now_time,
#             "exercise": exercise["name"].title(),
#             "duration": exercise["duration_min"],
#             "calories": exercise["nf_calories"]
#         }
#     }
#
#     sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
params = {
    "workout": {
        "date": today_date,
        "time": now_time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories}
}

response = requests.post(SHEETY_URL, json=params, verify=False)
