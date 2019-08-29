from bloomfilter import BloomFilter 
from random import shuffle 

#items_count should be the same as count of unique words
items_count = 1386991
falsepositive_probability = 0.001

# words to be added 
tamil_words = ['மதுரை','முக்குறுணிப்','பிள்ளையார்','சன்னிதி','மீனாட்சி', 
				'அம்மன்','கோவிலில்','அமைந்துள்ளது','சன்னதிக்கும்','சுந்தரேசுவரர்','இடையே']

# word not added 
english_words = ['hello','how','are','you','doing'] 


bloom_read = BloomFilter(items_count,falsepositive_probability,"/home/ANANT/msankarasubbu/Documents/Work/opensource/Data/tamil_words_filter.txt")

jumbled_words = tamil_words[:10] + english_words 
shuffle(jumbled_words) 
for word in jumbled_words: 
	if bloom_read.check(word): 
		if word in english_words: 
			print("'{}' is a false positive!".format(word)) 
		else: 
			print("'{}' is probably present!".format(word)) 
	else: 
		print("'{}' is definitely not present!".format(word)) 