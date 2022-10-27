import requests
from twilio.rest import Client

MY_LATITUDE = 44.786568
MY_LONGITUDE = 20.448921

ACCOUNT_SID = "AC2d723e8087ebbe30726ea3f1993949f5"
AUTH_TOKEN = "096803341e67304dd7c3d023c78641a8"

parameters = {"lat": MY_LATITUDE,
              "lon": MY_LONGITUDE,
              "appid": "a3dea942510e803422164a2de50213fb",
              "q": "Mar del Plata"
              }

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
weather = response.json()
weather_code = weather["weather"][0]["id"]
if weather_code < 600:
    print("Hard rain is gonna fall")

client = Client(ACCOUNT_SID, AUTH_TOKEN)
message = client.messages \
                .create(
                     body="Get an umbrella.",
                     from_='+381 62 9381122',
                     to='Your verified phone number'
                 )

print(message.status)



