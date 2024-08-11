from twilio.rest import Client

# Your Twilio account SID and Auth Token
account_sid = 'AC9bfafc79a01522a0f7ed67d4b3b529b2'
auth_token = 'f0c7cec9f3e8f34a806db22adcc161e0'

# Initialize the Twilio Client
client = Client(account_sid, auth_token)

# Define the call parameters
call = client.calls.create(
    to='+918707640055',  # The Indian phone number you want to call
    from_='+19388674106', # Your Twilio phone number
    url='http://demo.twilio.com/docs/voice.xml'  # A URL that returns TwiML instructions
)

print(f"Call")