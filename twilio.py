# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC241dc2d3404310c4ac5b888fc7d57a03"
auth_token = "15ec52bdc131cc880e5ef057a3bda296"
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Bull Bull Mighty Bull",
  from_="+18442849659",
  to="+16364394068"
)
print(message.sid)