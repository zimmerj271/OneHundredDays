import smtplib
import os

class Emailer:
    def __init__(self):
        self.sender_email = "vikingsmash@yahoo.com"
        self.sender_pw = os.environ("YAHOO_PASSWORD")
        self.smtp_server = "smtp.mail.yahoo.com"

    def sendEmail(self, email, subject, message):
        msg = f"Subject:{subject}\n\n{message}"
        with smtplib.SMTP(self.smtp_server) as connection:
            connection.starttls()
            connection.login(user=self.sender_email, password=self.sender_pw)
            connection.sendmail(from_addr=self.sender_email, to_addrs=email, msg=msg)

