import datetime as dt
import pandas as pd
from random import choice
import smtplib
##################### Extra Hard Starting Project ######################
birthdays_df = pd.read_csv("birthdays.csv")

# 1. Update the birthdays.csv -- done

# 2. Check if today matches a birthday in the birthdays.csv
def check_birthday(df):
    current_date = dt.date.today()
    for index, row in df.iterrows():
        birthday = dt.date(year=row.year, month=row.month, day=row.day)
        if current_date.day == birthday.day and current_date.month == birthday.month:
            contact_info = (row[0], row[1])
            return contact_info
        else:
            return False

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv


def random_letter(name):
    letters = ('letter_1.txt', 'letter_2.txt', 'letter_3.txt')
    with open(f"letter_templates/{choice(letters)}", mode="r") as letter_file:
        letter = letter_file.readlines()
    letter[0] = letter[0].replace('[NAME]', name)
    return letter

# 4. Send the letter generated in step 3 to that person's email address.
def send_email(email, message):
    my_email = "vikingsmash@yahoo.com"
    password = "qgyxtfldhrwczwiw"
    smtp_server = "smtp.mail.yahoo.com"
    with smtplib.SMTP(smtp_server) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=message)


birthday_person = check_birthday(birthdays_df)
if birthday_person:
    name = birthday_person[0]
    email = birthday_person[1]
    letter = random_letter(name)
    msg = "Subject:Happy Birthday\n\n" + "\n".join(letter)
    send_email(email, msg)
else:
    print("Today is not your birthday")



