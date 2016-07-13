balance = 3926
annualInterestRate = 0.2

#import time

monthlyInterest = annualInterestRate / 12.0
workingBalance = balance

minimumPayment = 0

while workingBalance > 0:
	minimumPayment += 10
	workingBalance = balance
	for month in range(1, 13):
		workingBalance -= minimumPayment
		workingBalance = workingBalance + (workingBalance * monthlyInterest)
		# print month
		# print minimumPayment
		# print workingBalance
#		time.sleep(0.01)
	

print "Lowest Payment: " + str(minimumPayment)
