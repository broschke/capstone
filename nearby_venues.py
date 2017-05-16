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

CLIENT_ID = ID
CLIENT_SECRET = SECRET

url_venue = "https://api.foursquare.com/v2/venues/explore?"
near = 'll=38.9,-77.0'
radius = '500'
v = "20140806"
m = "foursquare"

url_composite = url_venue + "client_id=" + CLIENT_ID + "&" + "client_secret=" + CLIENT_SECRET + "&" + near + "&" + radius + "&" + "v=" + v + "&" + "m=" + m
contents = urllib.request.urlopen(url_composite).read()

parsed = json.loads(contents)

pprint.pprint(parsed)