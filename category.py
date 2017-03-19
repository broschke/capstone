import urllib.request
import json 
import sqlite3
from key import ID, SECRET

CLIENT_ID = ID
CLIENT_SECRET = SECRET
v = '20170315'

url = 'https://api.foursquare.com/v2/venues/categories?client_id='+ CLIENT_ID +'&client_secret=' + SECRET + '&v=' + v

contents = urllib.request.urlopen(url).read()

#print(contents)

parsed = json.loads(contents)

#for i in parsed['response']['categories']:
#    print(i['id'])
#print(i)

#print(parsed['response'][0]['categories']['categories']['id'])
for i in parsed['response']['categories']:
    print(i['id'])