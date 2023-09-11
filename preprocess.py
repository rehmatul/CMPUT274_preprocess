#--------------------------------------------
#   Name: Fatima Rehmatullah
#   ID: 1631703
#   CMPUT 274, Fall 2020
#
#   Weekly Exercise #4: Text Preprocessor
#-------------------------------------------- 

# NOTE:  Make sure all of your functions are properly documents
#   (e.g., with docstrings)

import sys

def fullpreprocessing():
	"""Inputs a string from the user and processes it to remove punctuation, symbols and digits and return a processed string
	Arguments:
	Returns none but outputs the processed string to the terminal.
	"""
	inputlist=list(map(str,input().split()))
	#calls the lower function to convert the list elements to lowercase
	lowerlist=lowercase(inputlist)
	#the punctuation function removes all special characters
	alphanumericlist=punctuation(lowerlist)
	#removes all digits
	numberlist=numbers(alphanumericlist)
	#removes all stop word
	stoplist=stopwords(numberlist)
	#prints the processed list
	print(*stoplist)

def modeanderrorhandling():
	"""Reads the command line input and performs what the user wants: full preprocessing or just some steps.
	Reads the command line input and calls relevant functions to perform the tasks.
	Also checks if a command line input is in the wrong format, incomplete or contains extra words.
	Arguments: 
	Returns none but gives an error message for incorrect command line input.
	"""

	if len(sys.argv) == 2:
		#checks if the mode is given and processes it to check the mode if it is
		mode=sys.argv[1]
		#performs all processes while keeping digits
		if mode=="keep-digits":
			inputlist=list(map(str,input().split()))
			lowerlist=lowercase(inputlist)
			alphanumericlist=punctuation(lowerlist)
			stoplist=stopwords(alphanumericlist)
			print(*stoplist)
		#performs all processes while keeping stop words
		elif mode=="keep-stops":
			inputlist=list(map(str,input().split()))
			lowerlist=lowercase(inputlist)
			alphanumericlist=punctuation(lowerlist)
			numberlist=numbers(alphanumericlist)
			print(*numberlist)
		#performs all processes while keeping symbols
		elif mode=="keep-symbols":
			inputlist=list(map(str,input().split()))
			lowerlist=lowercase(inputlist)
			numberlist=numbers(lowerlist)
			stoplist=stopwords(numberlist)
			print(*stoplist)
		#prints an error and exits if an incorrect mode is given
		else:
			print("ERROR: The mode you entered is incorrect")
			print("Enter in the format: 'python3 preprocess.py <mode>")
			print("Where mode can be 'keep-digits','keep-stops' or 'keep-symbols'")
			sys.exit(1)
	#performs full preprocessing if no mode specified
	elif len(sys.argv)==1:
		fullpreprocessing()
	#gives an error message and quitis if more than one word used for mode
	elif len(sys.argv)>2:
		print("ERROR: Your command has too many arguments.")
		print("Enter in the format: 'python3 preprocess.py <mode>")
		print("Where mode can be 'keep-digits','keep-stops' or 'keep-symbols'")
		sys.exit(1)



def lowercase(inputlist):
	"""Analyses the input list and converts all elements to lower case.
	Arguments:
	Takes the list inputted by the user as a parameter
	Returns the inputlist with all the elements converted to lower case
	"""
	#returns an error message if the input is empty

	if inputlist==[]:
		print("Please enter an input string")
		sys.exit(1)
	for i in range(len(inputlist)):
		inputlist[i]=inputlist[i].lower()
	return(inputlist)	

def punctuation(inputlist):
	"""Analyses the list one word at a time and removes all special characters
	Arguments:
	Takes a list as a parameter
	Returns a new list in which there are no special characters
	"""
	alphanumericlist=[]
	#loop through the list and then loops through each word
	newword=""
	for i in range(len(inputlist)):
		for character in inputlist[i]:
			#anaylses one character at a time to remove any special characters
			if character.isalnum():
				newword=newword+character
		alphanumericlist.append(newword)
		newword=""
	return(alphanumericlist)

def numbers(inputlist):
	"""Analyses the list one word at a time and removes all digits from the words unless a word is completely made of digits.
	Arguments:
	Takes the list as a parameter
	Returns a newlist with all the digits removed from the words.
	"""
	numberlist=[]
	numberword=""
	numbers=['0','1','2','3','4','5','6','7','8','9']
	#loops through the list parameter and analyses one word at a time
	for i in range(len(inputlist)):
		for character in inputlist[i]:
		#loops through each word to removes digits
			if character in numbers:
				numberword=numberword
			else:
				numberword=numberword+character
		#if all the characters are digits, newword is just the original word
		if numberword=="":
			numberlist.append(inputlist[i])
		else:
			numberlist.append(numberword)
		numberword=""
	return(numberlist)

def stopwords(inputlist):
	"""Analyses the list one word at a time and removes all the stop words.
	Arguments:
	Takes the list as a parameter
	Returns a newlist with all the stop words removed
	"""
	stoplist=[]
	stopwords=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", 
"yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", 
"hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", 
"themselves", "what", "which","who", "whom", "this", "that", "these", "those", 
"am", "is", "are", "was", "were", "be","been", "being", "have", "has", "had", 
"having", "do", "does", "did", "doing", "a", "an","the", "and", "but", "if", 
"or", "because", "as", "until", "while", "of", "at", "by", "for", "with", 
"about", "against", "between", "into", "through", "during", "before", "after", 
"above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over",
"under", "again", "further", "then", "once", "here", "there", "when", "where", 
"why", "how", "all", "any", "both", "each", "few", "more", "most", "other", 
"some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", 
"too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

	#loops through the parameter list and analyzes one word at a time, removes if the word is a stop word
	for i in range(len(inputlist)):
		if inputlist[i] not in stopwords:
			stoplist.append(inputlist[i])
	return(stoplist)


# You must determine how to structure your solution.
# Create your functions here and call them from under
# if __name__ == "__main__"!

if __name__ == "__main__":
	modeanderrorhandling()
	pass

    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 preprocess.py". This is directly relevant 
    # to this exercise, so you should call your code from here.
 