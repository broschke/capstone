import urllib.request
import json 
import sqlite3 as lite
from key import ID, SECRET
from pprint import pprint

con = lite.connect('foursquare.db')
cur = con.cursor()

CLIENT_ID = ID
CLIENT_SECRET = SECRET
v = '20170315'

url = 'https://api.foursquare.com/v2/venues/categories?client_id='+ CLIENT_ID +'&client_secret=' + SECRET + '&v=' + v

contents = urllib.request.urlopen(url).read()

parsed = json.loads(contents)
 

def get_categories(data):
    result = {}
    for cat in data:
        result[cat['id']] = cat['name']
        if cat['categories']:
            result.update(get_categories(cat['categories']))
    return result

categories = get_categories(parsed['response']['categories'])
#pprint(categories)
cat_tuple = [(k, v) for k, v in categories.items()]
#print(cat_tuple)

with con:
    cur.executemany("INSERT INTO categories VALUES(?,?)", cat_tuple)

con.commit()
con.close()