from googleplaces import GooglePlaces, types, lang
import requests
import json
import math
import geopandas
import geopy
from geopy.geocoders import Nominatim

# convert address to lat and long

locator = Nominatim(user_agent="myGeocoder")
location = locator.geocode("Champ de Mars, Paris, France")
lat = location.latitude
lng = location.longitude

# Use your own API key for making api request calls
API_KEY = 'AIzaSyAOSYnT-58lZ9MyVhhITedPhBYGj-xvLyc'
 
# Initialising the GooglePlaces constructor
google_places = GooglePlaces(API_KEY)
 
# call the function nearby search with the parameters as longitude, latitude, radius and type of place which needs to be searched of
query_result = google_places.nearby_search(
        lat_lng ={'lat': 28.4089, 'lng': 77.3178},
        radius = 5000,
        types =[types.TYPE_HOSPITAL])
 
# If any attributions related with search results print them
if query_result.has_attributions:
    print (query_result.html_attributions)
 
 
# Iterate over the search results

# closest_hospital = (hospital_name, distance_to_hospital)
closest_hospital = (None, math.inf)

for place in query_result.places:
    distance = abs(place.geo_location['lat'] - lat) + abs(place.geo_location['lng'] - lng)
    if (closest_hospital[1] > distance):
        closest_hospital = (place.name, distance)

    
    print(place)
    # place.get_details()
    print (place.name)
    print("Latitude", place.geo_location['lat'])
    print("Longitude", place.geo_location['lng'])
    print()
