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
    
    text =i['text']
    text= re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text)
    tokens = nltk.word_tokenize(text)
    
    for word in tokens:
        
        print("{0}\t{1}".format(word,1))