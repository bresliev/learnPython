##################### Extra Hard Starting Project ######################
import pandas
import smtplib
import random
import datetime
import re

my_password = "ycngyrakpjgbhsxa"
my_email = "nikola.pythonista@gmail.com"


df = pandas.read_csv("birthdays.csv")
list_as_dict = df.to_dict("records")

now = datetime.datetime.now()
today = now.day
month = now.month
for row in list_as_dict:
    if row["month"] == month and row["day"] == today:
        letter = "letter_templates/letter_"+str(random.randint(1, 3))+".txt"
        with open(letter, "r") as letter:
            msg = letter.read()
            msg = re.sub("(?<=\[)(.*?)(?=\])", row["name"], msg)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=row["email"],
                                msg="Subject: Happy Birthday!\n"+msg)





