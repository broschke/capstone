#! /usr/bin/env python
import urllib.request
import json 
import pprint
import sqlite3
from key import ID, SECRET

url_venue = "https://api.foursquare.com/v2/venues/"
venue_id = "512f9781183f26d8006f53cb" 
CLIENT_ID = ID
CLIENT_SECRET = SECRET
v = "20140806"
m = "foursquare"

url_composite = url_venue + venue_id + "?" + "client_id=" + CLIENT_ID + "&" + "client_secret=" + CLIENT_SECRET + "&" + "v=" + v + "&" + "m=" + m
#print(url_composite)

contents = urllib.request.urlopen(url_composite).read()
#print(contents)

db = sqlite3.connect('foursquare.db')

parsed = json.loads(contents)
#print(json.dumps(parsed, indent=4, sort_keys=True))

id = parsed['response']['venue']['id']
venue = parsed['response']['venue']['name']
lat = parsed['response']['venue']['location']['lat']
lng = parsed['response']['venue']['location']['lng']
address = parsed['response']['venue']['location']['address']
city = parsed['response']['venue']['location']['city']
state = parsed['response']['venue']['location']['state']
zip_code = parsed['response']['venue']['location']['postalCode']
country = parsed['response']['venue']['location']['country']
phone = parsed['response']['venue']['contact']['phone']
twitter = '@'+parsed['response']['venue']['contact']['twitter']
category = parsed['response']['venue']['categories'][0]['name']
rating = parsed['response']['venue']['rating']
checkins_count = parsed['response']['venue']['stats']['checkinsCount']
users_count = parsed['response']['venue']['stats']['usersCount']
tip_count = parsed['response']['venue']['stats']['tipCount']

print(users_count)