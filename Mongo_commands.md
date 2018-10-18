# 874
Assignment codes

## Importing the data steps:
```
Command used: C: \Program Files\ MongoDB\ Server\ 4.0\ bin > .\mongoimport--db tweet_data--
collection Tweet--file C: \Users\ Lameware\ Documents\ Tweet.json--jsonArray 
```
## Connecting to mongo: .\mongo.exe
## Select DB: use tweet_data
- Write a MongoDB query that returns all the Tweets : db.Tweet.find().pretty()
- Write a MongoDB query to find one of your Tweets by name: db.Tweet.find({"user.name":"user 03"}).pretty()
- Update your two favourite Tweets to have two tags called ‘My number 1 Tweet’ and ‘My number 2 Tweet’. Show two
ways to do this. Do the first using update() and do the second using save().
  - db.Tweet.update({ "user.name":"user 03"},{ $set:{"entities.hashtags":"My Tweet number 1"}})
  - var mongo = db.Tweet.findOne({"user.name":"user 24"});
    mongo["entities"]["hashtags"]="My tweet number 2"
    db.Tweet.save(mongo)
 - Write a MongoDB query that returns only Tweets that have tags: db.Tweet.find({"entities.hashtags":{$ne:[]}}).pretty()
 - Write a MongoDB query to find the Tweet Id for those Tweets which contain the keyword ‘health’ in their text: db.Tweet.find({"text":{$regex:/health/i}},{id_str:1}).pretty()
