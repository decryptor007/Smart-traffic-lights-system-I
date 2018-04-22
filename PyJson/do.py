#!/usr/bin/env python

#python adds a u' before each key 
#That is why your text is type unicode not string. Most time it is better to have text in unicode for german umlauts and //
#for sharing text results with other modules/programs etc

import json
from pprint import pprint

with open('data.json') as data_file:    
    data = json.load(data_file)
    text=data["masks"]["id"]
print(text)

# if we need 
#data["maps"][0]["id"]  # will return 'blabla'
#data["om_points"]      # will return 'value'

#Done By Mazen
