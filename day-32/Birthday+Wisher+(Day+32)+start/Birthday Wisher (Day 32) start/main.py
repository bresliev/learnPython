<<<<<<< HEAD
import datetime as dt
import smtplib
import random

my_password = "ycngyrakpjgbhsxa"
my_email = "nikola.pythonista@gmail.com"

with open("quotes.txt") as f_quotes:
    quotes = f_quotes.readlines()
print(quotes)
day_of_the_week = dt.datetime.now().weekday()

if day_of_the_week == 1:
    msg = f"Subject: motivation\n\n{random.choice(quotes)}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="nikola.bresliev@gmail.com",
                            msg=msg)
=======
import smtplib

my_email = "nikola.pythonista@gmail.com"
password = "ipezmywwuljoynfx"
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.ehlo()
connection.starttls()
connection.ehlo()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="nikola.bresliev@gmail.com", msg="Hello breee!!!")
>>>>>>> main
