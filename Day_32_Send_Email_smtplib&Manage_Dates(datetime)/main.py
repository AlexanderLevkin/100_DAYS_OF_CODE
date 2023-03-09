import smtplib

# my_email = "arterial888@gmail.com"
# recipient_email = "alexanderlevkin@yahoo.com"
# password = "odqvzefbnzuoocaa"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs=recipient_email,
#                         msg="Subject:Hello\n\nThis is the body of my email.")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_the_week = now.weekday()
print(day_of_the_week)
print(year)

day

