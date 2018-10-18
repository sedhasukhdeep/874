import json
import sys
import nltk
import re

#(\/\*\s+(\d+)\s+\*\/) <- remove /* 1*/
#(\"([^\"]+)\"\s+\:\s+(\w+)\(\"([^\"]+)\"\)\,) <- remove object id
#(\"([^\"]+)\"\s+\:\s+(\w+)\((\d+)\)\,)<- remove id



with open('10000 tweets_old.json', 'r', encoding="utf8") as f:
    data = json.load(f)


    
    
    
    
for i in data:
    try:
        text= i['gnip']['profileLocations'][0]['address']['country']
    #text= i['actor']['twitterTimeZone']
    
        #i:f(text == 'Sydney'|'Melbourne'|'Victoria'|'Adelaide'|'Perth'|'Brisbane')
    except KeyError:
        text="Null"
        continue
    
    if(text=="Australia"):
        
        text= i['actor']['twitterTimeZone']
        
        
        print("{0}\t{1}".format(text,1))