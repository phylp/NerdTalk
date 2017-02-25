# Uses python3
# Given a list of price per clicks (a) and a list of clicks per day (b), find the total revenue after values from a and b are paired to maximize revenue 
# Safe move: find the highest click per pay price, and associate that with the highest available click per day  

import sys

def max_dot_product(a, b):
	revenue = 0
	while len(a) > 0 and len(b) > 0:
		greatest_price = max(a)
		greatest_frequency = max(b)
		a.remove(greatest_price)
		b.remove(greatest_frequency)
		revenue += (greatest_price * greatest_frequency)
	return revenue

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
