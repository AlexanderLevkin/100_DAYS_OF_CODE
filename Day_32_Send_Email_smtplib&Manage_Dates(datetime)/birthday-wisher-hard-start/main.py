##################### Normal Starting Project ######################
import datetime as dt
import random

import pandas as PD
import smtplib
my_email = "arterial888@gmail.com"
password = "odqvzefbnzuoocaa"

today = (dt.datetime.now().month, dt.datetime.now().day)

# HINT 2: Use pandas to read the birthdays.csv
data = PD.read_csv("birthdays.csv")

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in birthdays_dict:
    birthdays_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthdays_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthdays_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")
