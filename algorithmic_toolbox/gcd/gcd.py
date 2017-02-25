#naive solution implements exhaustive enumeration to find the greatest common divisor
def gcd_naive(a,b):
	greatest = 0
	for i in range(0, a+b):
		if i % a == 0 and i % b == 0:
			greatest = i
	return greatest

#euclidean solution, implements key lemma of 'a' prime
def gcd_euc(a,b):
	if b == 0: 
		return a	
	prime = a % b
	return gcd_euc(b, prime)
