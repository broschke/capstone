# -*- coding: utf-8 -*-
"""
Created on Tue May  2 17:23:16 2017

@author: Bernardo.Roschke
"""

import urllib.request
import json 
import pprint
from pathlib import Path
import os
from key import ID, SECRET

url_venue = "https://api.foursquare.com/v2/venues/"
venue_id = "512f9781183f26d8006f53cb" 
CLIENT_ID = ID
CLIENT_SECRET = SECRET
v = "20140806"
m = "foursquare"

url_composite = url_venue + venue_id + "?" + "client_id=" + CLIENT_ID + "&" + "client_secret=" + CLIENT_SECRET + "&" + "v=" + v + "&" + "m=" + m

contents = urllib.request.urlopen(url_composite).read()

parsed = json.loads(contents)

id = parsed['response']['venue']['id']
venue = parsed['response']['venue']['name']
rating = parsed['response']['venue']['rating']
checkins_count = parsed['response']['venue']['stats']['checkinsCount']
users_count = parsed['response']['venue']['stats']['usersCount']

venue_file = os.path.join(os.getcwd(),'venues.json')
if not Path(venue_file).is_file():
    file = open(venue_file,'x')
    
else:
    file = open(venue_file,'w')

venue_dict = {"id": id, "venue": venue, "rating": rating, "checkins_count": checkins_count, "users_count": users_count, "popular": checkins_count / users_count}

json.dump(venue_dict, file)

file.close()
