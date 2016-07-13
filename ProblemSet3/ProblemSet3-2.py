secretWord = 'apple'

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's'] 

# Include this definition
def isWordGuessed(secretWord, lettersGuessed):
	for character in secretWord:
		if character not in lettersGuessed:
			return False
	return True

# Do not include below

print isWordGuessed(secretWord, lettersGuessed)