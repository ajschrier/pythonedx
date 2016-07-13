secretWord = 'apple'

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

#Include this definition

def getGuessedWord(secretWord, lettersGuessed):
	guessedWord = ''
	for character in secretWord:
		if character in lettersGuessed:
			guessedWord += character
		else:
			guessedWord += '_ '
	return guessedWord

# Debug only

print getGuessedWord(secretWord, lettersGuessed)