# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"

client = Client(account_sid, auth_token)

# A list of account objects with the properties described above
accounts = client.api.accounts.list(friendly_name="MySubaccount")

for account in accounts:
    print(account.sid)
