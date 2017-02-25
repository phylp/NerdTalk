# Uses python3
# Find the miniumum number of coins needed to change the input value (an integer) into coins with denominations of 1, 5, 10 
# Safe move: take highest denomination d where d < amount remaining, then add d to count, then repeat process with amount - denomination    

import sys

def get_change(amount):
	denominations = [10,5,1]
	count = 0
	for i in denominations:
		while i <= amount:
			amount -= i
			count += 1
	return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))