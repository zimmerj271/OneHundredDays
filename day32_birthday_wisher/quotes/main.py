import smtplib
import datetime as dt
from random import choice

my_email = "vikingsmash@yahoo.com"
password = "qgyxtfldhrwczwiw"
smtp_server = "smtp.mail.yahoo.com"
receiver_email = "zimmerju@gmail.com"

# connection = smtplib.SMTP(smtp_server)
# connection.starttls()  # start Transport Layer Security (TLS) encryption
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email,
#                     to_addrs="zimmerju@gmail.com",
#                     msg="Subject:Howdy\n\nThis is the body of my email.")
# connection.close()

current_time = dt.datetime.now()

if current_time.day == 2:
    with open("quotes.txt", mode="r") as file:
        quotes = file.readlines()

    message = f"Subject:Daily Quote\n\n{choice(quotes)}"
    with smtplib.SMTP(smtp_server) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=receiver_email, msg=message)
