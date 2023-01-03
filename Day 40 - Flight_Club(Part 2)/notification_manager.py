import os
import smtplib
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

TWILIO_SID = os.getenv('TW_SID')
TWILIO_AUTH_TOKEN = os.getenv('TW_AUTH_TOKEN')
TWILIO_VIRTUAL_NUMBER = os.getenv('TW_VR_NUMBER')
TWILIO_VERIFIED_NUMBER = os.getenv('TW_VF_NUMBER')
MAIL_PROVIDER_SMTP_ADDRESS = os.getenv('MAIL_PROVIDER_SMTP_ADDRESS')
USER_EMAIL = os.getenv('USER_EMAIL')
USER_PASSWORD = os.getenv('USER_PASSWORD')

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

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as conn:
            conn.starttls()
            conn.login(USER_EMAIL, USER_PASSWORD)
            for email in emails:
                conn.sendmail(
                    from_addr=USER_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )