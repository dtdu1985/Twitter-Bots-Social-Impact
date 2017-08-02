# Each word in the lexicon has scores for:
# 1)     polarity: negative vs. positive    (-1.0 => +1.0)
# 2)    subjectivity: objective vs. subjective (+0.0 => +1.0)


import tweepy
from textblob import TextBlob
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
tweets = api.search(q=“#Bitcoin”,lang="en")


for tweet in tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    results = TextBlob(tweet.text)
    print(results.sentiment)

    if results.sentiment.polarity < 0:
        sentiment = "sentiment: negative"
    elif results.sentiment.polarity == 0:
        sentiment = "sentiment: neutral"
    else:
        sentiment = "sentiment: positive"
    print sentiment
    print("")

   
    


    

 
