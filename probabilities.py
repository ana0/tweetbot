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


cats = split_words("pg7885.txt")
ok = probabilities_matrix(cats)

print ok