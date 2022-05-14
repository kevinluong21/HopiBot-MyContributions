import os
from twilio.rest import Client 

# NO CLUE WHAT THIS PART IS FOR BUT WE CAN JUST KEEP IT :D

account_sid = 'AC41e0182be023d4100adb8c6928fdca7f' 
auth_token = '1e8b2418b4920164ed2756dca1a63278' 
client = Client(account_sid, auth_token) 

class  Phone():
    sid = 'MGf240f55269be853d1089f92e87860b1d'

    #IS THIS HOW UR SUPPOSED TO USE INIT???
    def __init__ (self, hospital, time, number):
        self.hospital = hospital
        self.time = time
        self.number = number

    def send_message(self):
        message = client.messages.create(  
                              messaging_service_sid='MGf240f55269be853d1089f92e87860b1d', 
                              body='Please arrive at' + self.hospital + 'in' + self.time + 'minutes',      
                              to='+' + self.number
                          )
        print(message.sid) #this isnt needed right?

