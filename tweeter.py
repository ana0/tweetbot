import tweepy
import twitterkeys
# import nltk.data

class TwitterAPI:
    def __init__(self):
        auth = tweepy.OAuthHandler(twitterkeys.consumer_key, twitterkeys.consumer_secret)
        auth.set_access_token(twitterkeys.access_token, twitterkeys.access_token_secret)
        self.api = tweepy.API(auth)
 
    def tweet(self, message):
        self.api.update_status(status=message)

tweet = "Hello World"


twitter = TwitterAPI()
twitter.tweet(tweet)