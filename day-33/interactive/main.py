import requests

MY_LAT = 44.786568
MY_LNG = 20.448921
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# latitude = data["iss_position"]["latitude"]
# print(data)
# print(latitude)

parameters = {"lat": MY_LAT,
              "lng": MY_LNG,
              "formatted": 0}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise_h = (data["results"]["sunrise"]).split("T")[1].split(":")[0]
sunset_h = (data["results"]["sunset"]).split("T")[1].split(":")[0]
print(sunrise_h)
print(sunset_h)
