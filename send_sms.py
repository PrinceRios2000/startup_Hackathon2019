# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import os

def sendText():
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    
    message = client.messages \
                    .create(
                         body="Your power will be cut by 5:00 PM.",
                         from_='+12512500792',
                         to='+18316826544'
                     )
    print(message.sid)
