# -*- coding: utf-8 -*-
"""
Created on Tue May  2 17:23:16 2017

@author: Bernardo.Roschke
"""

import json
from pathlib import Path
import os

venue_file = os.path.join(os.getcwd(),'test.txt')
if not Path(venue_file).is_file():
    file = open(venue_file,'x')
    file.write('hello world')
else:
    file = open(venue_file,'w')
    file.write('hello world, file already exists')


file.close()

reader = open(venue_file, 'r')
print(reader.read())

reader.close()