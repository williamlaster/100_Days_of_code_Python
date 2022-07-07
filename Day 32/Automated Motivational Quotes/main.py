import datetime as dt
import smtplib
import random


# Picking Quotes
with open(file="quotes.txt") as quotes_file:
    quotes = quotes_file.read()
    quote_list = quotes.split('\n')

picked_quote = random.choice(quote_list)

# Date & Time
now = dt.datetime.now()
weekday = now.weekday()


# From Email Information
my_email = "Enter Your Email Addres Here"
my_password = "Enter Your Email Password Here"

# weekday of 0 = Monday, 1 = Tuesday, 2 = Wednesday.....
if weekday == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="Place Your Target Email Here",
            msg=f"Subject:Test - Automated Email - Test\n\n{picked_quote} - This is an automated email"
        )
