import requests
from datetime import datetime
import smtplib

MY_LAT = -136.4175  # Your latitude
MY_LONG = 43.0817  # Your longitude
##-137.5112
#42.5466
MY_PASSWORD = "ycngyrakpjgbhsxa"
MY_FROM_EMAIL = "nikola.pythonista@gmail.com"
MY_TO_EMAIL = "nikola.bresliev@gmail.com"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

print(data)
print(iss_longitude)
print(iss_latitude)
print(time_now.hour)
print(sunset)
print(sunrise)

if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 and sunset < time_now.hour < sunrise:  # sunset < time_now.hour < sunrise:
    connection = smtplib.SMTP("smtp.gmail.com")

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.login(user=MY_FROM_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_FROM_EMAIL, to_addrs=MY_TO_EMAIL,
                            msg="Subject: ISS over your head!\n" + "Get up and look up!!!")


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
