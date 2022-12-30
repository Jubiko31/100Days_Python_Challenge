import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

TWILIO_SID = os.getenv('TW_SID')
TWILIO_AUTH_TOKEN = os.getenv('TW_AUTH_TOKEN')
TWILIO_VIRTUAL_NUMBER = os.getenv('TW_VR_NUMBER')
TWILIO_VERIFIED_NUMBER = os.getenv('TW_VF_NUMBER')

class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)
