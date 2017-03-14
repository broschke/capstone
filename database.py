import sqlite3 as lite

con = lite.connect('foursquare.db')
cur = con.cursor()

with con:
	cur.execute('CREATE TABLE venues (id INTEGER, venue TEXT, latitude REAL, logitude	REAL, address TEXT, city TEXT, state TEXT, zip INTEGER,	country	TEXT, phone	INTEGER, twitter TEXT, categories TEXT, rating REAL, checkins_count	INTEGER, users_count INTEGER, tip_count	INTEGER, PRIMARY KEY(id))')
	cur.execute('CREATE TABLE users (id	INTEGER, venue_id INTEGER, firstname TEXT, lastname	TEXT, gender TEXT, tip BLOB, PRIMARY KEY(id))')
