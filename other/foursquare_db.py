import sqlite3 as lite

con = lite.connect('foursquare.db')
cur = con.cursor()

with con:
	cur.execute("CREATE TABLE venues (id text, venue text, latitude real, longitude real, address text, city text, state text, zip text, country text, phone text, twitter text, category text,rating real, checkins_count integer, users_count integer, tip_count integer)")
	cur.execute("CREATE TABLE categories (id text, name text)")
