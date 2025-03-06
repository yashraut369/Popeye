import os
from twilio.rest import Client

class TwilioCalls:
    def __init__(self):
        self.client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
        self.from_phone = os.getenv("TWILIO_PHONE_NUMBER")

    def make_call(self, to_phone):
        call = self.client.calls.create(
            to=to_phone,
            from_=self.from_phone,
            url="http://demo.twilio.com/docs/voice.xml"
        )
        print(f"Call initiated with SID: {call.sid}")