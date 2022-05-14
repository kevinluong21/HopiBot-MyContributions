import os
from twilio.rest import Client 
 
account_sid = 'AC41e0182be023d4100adb8c6928fdca7f' 
auth_token = '1e8b2418b4920164ed2756dca1a63278' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MGf240f55269be853d1089f92e87860b1d', 
                              body='YOU GOT THIS! FIGHTING GURL!',      
                              to='+16132866588' 
                          ) 
 
print(message.sid)

# import os
# from twilio.rest import Client


# account_sid = os.environ.get('AC41e0182be023d4100adb8c6928fdca7f')
# auth_token = os.environ.get('1e8b2418b4920164ed2756dca1a63278')

# client = Client(account_sid, authtoken)

# client.messages.create(from=os.environ.get('+12347043104'),
#                       to=os.environ.get('+16132866588'),
#                       body='You just sent an SMS from Python using Twilio!')