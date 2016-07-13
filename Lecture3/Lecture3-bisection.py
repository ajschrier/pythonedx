print "Please think of a number between 0 and 100!"


guess = 0
upper = 100
lower = 0

userSelection = ""

while userSelection != "c":
	guess = (upper + lower) / 2
	print "Is your number " + str(guess) + "?"
	userSelection = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
	if userSelection == "c":
		break
	elif userSelection == "h":
		upper = guess
	elif userSelection == "l":
		lower = guess
	else:
		print "Sorry, I did not understand your userSelection."
		
print "Game over. Your secret number was: " + str(guess)

