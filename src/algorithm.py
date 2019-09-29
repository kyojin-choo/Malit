### algorithm.py -*- calculating the score -*-
# 
##  Author: Daniel Choo
##  Date:   09/28/19

import re
import sys
from profanity import badwords as bad
import importRedditUser as iru

def score():
	""" score(): assigns a score to a certain individual.
               The algorithm (subject to change.): 
	                   
             	                  curr. comment                          post hist.
	             sum((word freq * ((word freq / total words)*weight) + (word * weight))

	    returns: score (float: user's suspiciousness score 0.0-1.0)
	"""
	

	user_list = iru.main()

	# Importing in the profanity.py
	profanity = bad()

	# Loop to create naughty dict
	for users in user_list:

		# Initializing variables/Reset when you iter..
		naughty = {}
		profane_count = 0
		word_count = 0
		avg_bad = 0
		score = 0.0
		
		# Iterate through the comments in the object.
		for sentence in users.comments:
			for word in sentence.commentText():
				word = re.sub(r'[^\w\s]','',word)            # Regex substituting in "" for punctuation
				word_count+=1
				print(word)
				# Local profanity dict creation
				if word in profanity and word not in naughty:
					naughty[word] = 0                           # Add profanity to dict.
					profane_count+=1

				if word in naughty:
					naughty[word] += 1                          # Increment counter
					profane_count+=1
			
			print(user, "\n" , naughty)
					

			# Algorithm
			timeCheck = (user.numComments / (user.age/3600*24)) 

			if timeCheck >= 0.8:
				for i in naughty:				
					avg_bad+=(naughty[i] * profanity[i])
					
				avg_bad /= len(dict)
				score = (profanity_count*avg_bad)/(word_count*0.1)

			else:
				pass

			print(users.name, " has a suspicious score of ", score)

#		if score > 1.0:
#			score = 1.0
 
#		print(user_list[x])

	return 0

def menu():
	""" menu(): debugging purposes.
      returns: user_input (int)
	"""
	usr_input = -1

	# Bounds check
	while usr_input < 0 and usr_input <= 2:
		usr_input = int(input("Choose an option:\n1.) Run score test.\n2.) Exit\n\nSelect an option: "))

	return usr_input

def __test__():
	""" __test__(): hypothetical users and comments
	    return: 
	"""
	dummy = ["You fucking bitch i hate your living fucking guts", "this clusterfuck of kkk kikes wont shut the fuck up."]
	print(score(dummy))
	return 0

def main():

	check = False

	while check is False:
		x = menu()
	
		if x == 1:
			score()
			
		elif x == 2:
			sys.exit(0)

main()
