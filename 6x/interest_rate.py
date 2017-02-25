# Uses python3
# Given an annual interest rate (r), minimum monthly payment rate (m), and balance (b), find the balance owed after a year of minimum payments

def interest(r,m,b):
	for i in range(12):
		minimum = b * m
		b += ((r/12) * b)
		b -= minimum
	print('Balance due after one year: ' + str(b))
	return b


# Given annual rate r, and balance b, find the minimum monthly payment p required to pay off a balance at the end of the year
def minimum(r,b,p):
	b1 = b
	for i in range(11):
        interest = r/12
        monthlyunpaid = b1 - p
        b1 = monthlyunpaid + (interest * monthlyunpaid)
    if b1 <= p:
        print('Lowest payment: ' + str(p))
        return
    else: 
    	return minimum(r, b, p+10)


# Given annual rate r, and balance b, find the minimum monthly payment p required to pay off a balance at the end of the year to the nearest 10 cents
#Test Case: 

# Test Case 1:
# balance = 320000
# annualInterestRate = 0.2
# Lowest Payment: 29157.09

def minimum2(balance, annualInterestRate):
	def getPaymentResult(p):
		b1 = balance
		r = annualInterestRate
		for i in range(11):
			interest = r/12
			monthlyunpaid = b1 - p
			b1 = monthlyunpaid + (interest * monthlyunpaid)
		return b1

	lower = balance/12
	upper = (balance*((1+(annualInterestRate/12))**12)/12)

	result = 
	while result >= 1:
		guess = (upper + lower)/2
		result = getPaymentResult(guess)
		if result > guess :
			lower = guess
		elif result < guess:
			upper = guess
	return result



