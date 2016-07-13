balance = 320000
annualInterestRate = 0.2

monthlyInterest = annualInterestRate / 12.0
workingBalance = balance

minimumPayment = 0.0
tolerance = 0.01

lowerBound = balance / 12
upperBound = (balance * ((1.0 + monthlyInterest)**12)) / 12.0
solved = False

# print "base lower bound " + str(lowerBound)
# print "base upper bound " + str(upperBound)

while solved == False:
	minimumPayment = (lowerBound + upperBound) / 2
	#print minimumPayment
	workingBalance = balance
	for month in range(1, 13):
		workingBalance -= minimumPayment
		workingBalance = workingBalance + (workingBalance * monthlyInterest)
# 		print "month " + str(month) + " " + str(workingBalance)
# 	print "balance after check: " + str(workingBalance)
	if (upperBound - lowerBound) / 2 < tolerance or (balance - workingBalance == 0):
# 		print str(workingBalance)
# 		print "Lowest Payment: " + str(minimumPayment)
		solved = True
	
	if workingBalance < 0:
		upperBound = minimumPayment
# 		print "new upper bound " + str(upperBound)
# 		print "lower bound " + str(lowerBound) 
	else:
		lowerBound = minimumPayment
# 		print "upper bound " + str(upperBound)
# 		print "new lower bound " + str(lowerBound)
# 	print raw_input("")

print "Lowest Payment: " + str(round(minimumPayment, 2))
print "Published answer: 29157.09"