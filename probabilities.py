import random

def split_words(filename):
	text = open(filename, "r")
	text = text.read()
	text = text.replace("\r\n", " ")
	text = text.split(" ")
	return text

def probabilities_matrix(text):
	bigrams = {}
	for i in range(len(text)):
		try:
			if (text[i], text[i+1]) in bigrams:
				bigrams[(text[i], text[i+1])].append(text[i+2])
			else:
				bigrams[(text[i], text[i+1])] = [text[i+2]]
		except IndexError:
			return bigrams

def make_tweet(text):
	tweet = []
	#random.seed("cathadsfs")
	for word in random.choice(list(text.keys())):
		tweet.append(word)
	for i in range(23):
		random_word = random.randint(0, len(text[(tweet[i], tweet[i+1])])-1)
		tweet.append(text[(tweet[i], tweet[i+1])][random_word])
	return " ".join(tweet)

cats = split_words("pg7885.txt")
ok = probabilities_matrix(cats)
will_it_work = make_tweet(ok)

print will_it_work