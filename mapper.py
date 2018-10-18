import json
import sys
import nltk
import re
#Loading the clean Json file
with open('10000 tweets_old.json', 'r', encoding="utf8") as f:
 data = json.load(f)
#Iterating over the keys of the json dicionary

for i in data:

 text =i['text'] #This grabs the text key from the tweet
#Here we are passing it to tweet cleaning regex to remove things like special characters
and URL
 text= re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text)
#Using the NLTK tokenize function to generate tokens of the sentence

 tokens = nltk.word_tokenize(text)
#Outputting the Key Value pairs to STDIN
for word in tokens:

 print("{0}\t{1}".format(word,1)) 
