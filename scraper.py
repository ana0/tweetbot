# from bs4 import BeautifulSoup
# import urllib

# mytwitter = "https://twitter.com/ana0___"
# scraped = urllib.urlopen(mytwitter)
# soup = BeautifulSoup(scraped, "html.parser")

# print soup.encode('utf-8')

import tweepy
import twitterkeys
import nltk.data

# class TwitterAPI:
# 	def __init(self):
# 		auth = tweepy.OAuthHandler(twitterkeys.consumer_key, twitterkeys.consumer_secret_key)
# 		auth.set_access_token(twitterkeys.access_token, twitterkeys.access_token_secret_key)
# 		self.api = tweepy.API(auth)

# 	def make_tweet(self, message):
# 		self.api.update_status(status=message)

# tweet = "string"

auth = tweepy.OAuthHandler(twitterkeys.consumer_key, twitterkeys.consumer_secret_key)
auth.set_access_token(twitterkeys.access_token, twitterkeys.access_token_secret_key)
api = tweepy.API(auth)

# twitter = TwitterAPI
# twitter.make_tweet(tweet)

mytweets = api.user_timeline(screen_name='ana0___')
for tweet in mytweets:
	print tweet.text.encode("utf-8")

#initialize a list to hold all the tweepy Tweets
alltweets = []	

#make initial request for most recent tweets (200 is the maximum allowed count)
new_tweets = api.user_timeline(screen_name = 'ana0___',count=200)

#save most recent tweets
alltweets.extend(new_tweets)

#save the id of the oldest tweet less one
oldest = alltweets[-1].id - 1

#keep grabbing tweets until there are no tweets left to grab
while len(new_tweets) > 0:
	print "getting tweets before %s" % (oldest)
	
	#all subsiquent requests use the max_id param to prevent duplicates
	new_tweets = api.user_timeline(screen_name = 'ana0___',count=200,max_id=oldest)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#update the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	print "...%s tweets downloaded so far" % (len(alltweets))

outputtweets = [tweet.text.encode('utf-8') for tweet in alltweets]

# outputstring = ""

# for string in outputtweets:
# 	outputstring = outputstring + string.encode('utf-8')

# mytweets_as_corpus = nltk.word_tokenize(outputstring)

# print mytweets_as_corpus

with open('mytweets.txt', 'w') as f:
	for line in outputtweets:
		f.write(line + "/n")
