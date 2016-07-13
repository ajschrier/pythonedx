balance = 3000
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

grossAnnualPayments = 0.0
monthlyPayment = 0.0
monthlyInterest = annualInterestRate / 12.0

for month in range(1, 13):
	print "Month: " + str(month)
	monthlyPayment = monthlyPaymentRate * balance
	grossAnnualPayments += monthlyPayment
	print "Minimum monthly payment: " + str(round(monthlyPayment, 2))
	balance -= monthlyPayment
	
	balance = balance + (balance * monthlyInterest)
	print "Remaining balance: " + str(round(balance, 2))

print "Total annual payments: " + str(round(grossAnnualPayments, 2))
print "Balance remaining: " + str(round(balance, 2))