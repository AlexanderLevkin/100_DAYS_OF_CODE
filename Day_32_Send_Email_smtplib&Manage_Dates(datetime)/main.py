import smtplib
import random

my_email = "arterial888@gmail.com"
recipient_email = "alexanderlevkin@yahoo.com"
password = "odqvzefbnzuoocaa"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs=recipient_email,
#                         msg="Subject:Hello\n\nThis is the body of my email.")

import datetime as dt

now = dt.datetime.now()
# year = now.year
# month = now.month
# print(day_of_the_week)
# print(year)
#
# date_of_birth = dt.datetime(year=1991, month=12, day=15, hour=4)
# print(date_of_birth)

# ---------------------------------------IF DAY IS SAT THE EMAIL SEND----------------------------#
with open("quotes.txt") as file:
    list_of_quotes = [quote for quote in file.readlines()]

day_of_the_week = now.weekday()

if day_of_the_week == 5:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=recipient_email,
                            msg=random.choice(list_of_quotes))
else:
    print("This is not Monday")
