# -*- coding: utf-8 -*-

#reference: script is based on Shreyans Shrimal, available at https://github.com/shreyans29/thesemicolon

import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import re
from credentials import * 

"# -- coding: utf-8 --"

def calctime(a):
    return time.time()-a

positive=0
negative=0
compound=0

count=0
initime=time.time()
plt.ion()
#plt.ion gives interactive plotting


class listener(StreamListener):
    
    def on_data(self,data):
        global initime
        t=int(calctime(initime))
        #data is stored in json form
        all_data=json.loads(data)
        tweet=all_data["text"].encode("utf-8")
        #username=all_data["user"]["screen_name"]
        #get tweet in text and strip emoticons and extra items to just alphabet letters
        #pass words to blob variable
        tweet=" ".join(re.findall("[a-zA-Z]+", tweet))
        blob=TextBlob(tweet.strip())

        #declare global sentiment variables to get cumulative effect
        #compound is total sentiment
        global positive
        global negative     
        global compound  
        global count
        
        count=count+1
        #blob calculate sentiment for EACH sentence in tweet and adding it to senti var
        senti=0
        for sen in blob.sentences:
            senti=senti+sen.sentiment.polarity
            if sen.sentiment.polarity >= 0:
                positive=positive+sen.sentiment.polarity   
            else:
                negative=negative+sen.sentiment.polarity  
        compound=compound+senti        
        print count
        print tweet.strip()
        print senti
        print t
        print str(positive) + ' ' + str(negative) + ' ' + str(compound) 
        
        #set axis for x and y axis
        plt.axis([ 0, 70, -20,20])
        plt.xlabel('Time')
        plt.ylabel('Sentiment')
        plt.plot([t],[positive],'go',[t] ,[negative],'ro',[t],[compound],'bo')
        plt.show()
        plt.pause(0.0001)
        if count==200:
            return False
        else:
            return True
        
    def on_error(self,status):
        print status


auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

#if count is 200, then stop listener
twitterStream=  Stream(auth, listener(count))
#track a search that is frequent
twitterStream.filter(track=[“cryptocurrency”])
