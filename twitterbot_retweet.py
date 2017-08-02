#Notes
#import twitter API wrapper, API credentials from separate file 
#auth_handler  authentication handler to be used
#runs Tweet actions for hashtag word in local language top items
#api.search q the search query string
#lang Restricts tweets to the given language
#rppnumber of tweets to return per pg max 100 

import tweepy
from time import sleep
from credentials import *

#assign Twitter API app account credentials from a separate file for security
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#define Tweet search function with parameters
def searchtweet(api,searchterm,no_tweets): 

	for tweet in tweepy.Cursor(api.search, q=searchterm, lang='en').items(no_tweets):
    		try:
                        print('\nTweet by: @' + tweet.user.screen_name)
	
                        #retweet the user who tweeted
                        tweet.retweet()
        		print('Retweeted the tweet')

       			 # Favorite the tweet
        		tweet.favorite()
        		print('Favorited the tweet')

        		# Follow the user who tweeted
        		if not tweet.user.following:
                                tweet.user.follow()
                                print('Followed the user')

        		sleep(5) #Twitter actions every 5 seconds

    		except tweepy.TweepError as e:
        		print(e.reason)

    		except StopIteration:
        		break


#call function with desired hashtag and number of tweets to search
searchtweet(api,’#DoddFrank’,15)
