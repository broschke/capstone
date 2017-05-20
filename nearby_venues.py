# -*- coding: utf-8 -*-
"""
Created on Mon May 15 20:50:00 2017

@author: Bernardo.Roschke
"""

import urllib.request
import json 
import pprint
from pathlib import Path
import os
from key import ID, SECRET
import time

CLIENT_ID = ID
CLIENT_SECRET = SECRET

explore_url_venue = "https://api.foursquare.com/v2/venues/explore?"
near = 'll=38.9,-77.0'
radius = '1000'
v = "20140806"
m = "foursquare"

explore_url_composite = explore_url_venue + "client_id=" + CLIENT_ID + "&" + "client_secret=" + CLIENT_SECRET + "&" + near + "&" + radius + "&" + "v=" + v + "&" + "m=" + m
contents = urllib.request.urlopen(explore_url_composite).read()

explore_parsed = json.loads(contents)

venue_id = explore_parsed['response']['groups'][0]['items']

venue_list = [i['venue']['id'] for i in venue_id]

# print(venue_list)
ids = []
venue = []
rating = []
checkins_count = []
users_count = []

url_venue_base = "https://api.foursquare.com/v2/venues/"

for i in venue_list:
	url = url_venue_base + i + "?" + "client_id=" + CLIENT_ID + "&" + "client_secret=" + CLIENT_SECRET + "&" + "v=" + v + "&" + "m=" + m
	contents = urllib.request.urlopen(url).read()
	parsed = json.loads(contents)
	ids.append(parsed['response']['venue']['id'])
	venue.append(parsed['response']['venue']['name'])
	rating.append(parsed['response']['venue']['rating'])
	checkins_count.append(parsed['response']['venue']['stats']['checkinsCount'])
	users_count.append(parsed['response']['venue']['stats']['usersCount'])
	time.sleep(1)

print(users_count)