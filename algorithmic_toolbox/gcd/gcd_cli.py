import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

def gcd(a,b):
	if b == 0: 
		return a
	prime = a % b
	return gcd(b, prime)

print(gcd(a,b))