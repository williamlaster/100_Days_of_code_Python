import smtplib
import random
import pandas
import datetime as dt


today = (dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}


if today in birthdays_dict:
    person = birthdays_dict[today]
    letter_file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(letter_file_path) as letter_file:
        contents = letter_file.read()
        letter = contents.replace("[NAME]", person["name"])


EMAIL = "PUT YOUR EMAIL HERE"
PASSWORD = "PUT YOUR PASSWORD HERE"

# Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=EMAIL, to_addrs=person["email"],
        msg=f"Subject: Happy Birthday\n\n{letter}"
    )
