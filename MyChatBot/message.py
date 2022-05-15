import os
from twilio.rest import Client

from googleplaces import GooglePlaces, types, lang
import requests
import json
import math

API_KEY = 'AIzaSyDkvVLM_wuruRZGERL0ZsMCAWfgBarVrEQ'
account_sid = 'AC41e0182be023d4100adb8c6928fdca7f'
auth_token = '1e8b2418b4920164ed2756dca1a63278'
client = Client(account_sid, auth_token)

class Phone():
    sid = 'MGf240f55269be853d1089f92e87860b1d'

    # IS THIS HOW UR SUPPOSED TO USE INIT???
    def __init__(self, hospital, time, number):
        self.hospital = hospital
        # doctor or nurse inputs the time, but for now time is 10 minutes
        self.time = time
        self.number = number

    def send_message(self):
        message = client.messages.create(
            messaging_service_sid='MGf240f55269be853d1089f92e87860b1d',
            body='Please arrive at ' + self.hospital[0] + ' in ' + str(self.time) + ' minutes',
            to='+' + str(self.number)
        )


def get_lat_lng(address):
    lat, lng = None, None
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    endpoint = f"{base_url}?address={address}&key={API_KEY}"

    r = requests.get(endpoint)
    try:
        results = r.json()['results'][0]
        lat = results['geometry']['location']['lat']
        lng = results['geometry']['location']['lng']
    except:
        pass
    return lat, lng

# this will be used to get the address from the database
def get_address():
    return 0

# this will be used to get the address from the database
def get_number():
    return 0

def find_hospital():

    lat, lng = get_lat_lng(get_address())

    radius = 5000

    # Initialising the GooglePlaces constructor
    google_places = GooglePlaces(API_KEY)

    # call the function nearby search with the parameters as longitude, latitude, radius and type of place which needs to be searched of
    query_result = google_places.nearby_search(
        sensor = False,
        lat_lng={'lat': lat, 'lng': lng},
        radius=radius,
        types=[types.TYPE_HOSPITAL])

    # If any attributions related with search results print them
    if query_result.has_attributions:
        print(query_result.html_attributions)

    # Iterate over the search results

    # closest_hospital = (hospital_name, distance_to_hospital)
    closest_hospital = (None, math.inf)

    for place in query_result.places:
        distance = abs(float(place.geo_location['lat']) - lat) + abs(float(place.geo_location['lng']) - lng)
        if (closest_hospital[1] > distance):
            closest_hospital = (place.name, distance)

    return closest_hospital

# the 10 is temporary, just there bc we dont currently have a way to communicate with the hospital TT
text = Phone(find_hospital(), 10, get_number())
text.send_message()
