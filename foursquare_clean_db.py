# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 10:34:39 2017

@author: bernardo.roschke
"""

import sqlite3 as lite

con = lite.connect('foursquare.db')
cur = con.cursor()

with con:
    cur.execute('drop table if exists categories')