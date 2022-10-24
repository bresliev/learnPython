import smtplib

my_email = "nikola.pythonista@gmail.com"
password = "ipezmywwuljoynfx"
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.ehlo()
connection.starttls()
connection.ehlo()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="nikola.bresliev@gmail.com", msg="Hello breee!!!")