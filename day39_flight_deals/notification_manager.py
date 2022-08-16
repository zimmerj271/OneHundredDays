import os
from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.twilio_acc_sid = os.environ("TWILIO_SID")
        self.twilio_auth_token = os.environ("TWILIO_TOKEN")
        self.from_number = "+12166775599"
        self.to_number = "+12087809669"

    def send_message(self, msg):
        client = Client(self.twilio_acc_sid, self.twilio_auth_token)
        message = client.messages.create(
            body=msg,
            from_=self.from_number,
            to=self.to_number
        )
        print(message.status)
