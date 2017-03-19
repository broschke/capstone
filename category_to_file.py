import urllib.request
import json 
from key import ID, SECRET

CLIENT_ID = ID
CLIENT_SECRET = SECRET
v = '20170315'

url = 'https://api.foursquare.com/v2/venues/categories?client_id='+ CLIENT_ID +'&client_secret=' + SECRET + '&v=' + v

contents = urllib.request.urlopen(url).read()
outfile = open('category.json', 'w')

outfile.write(json.dumps(json.loads(contents.decode("utf-8")), indent=4, sort_keys=True))

