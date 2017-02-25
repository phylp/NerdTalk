#Uses python3
#recursive solution which is easy to read but computatationally inefficient
import sys

def fibonacci(num):
	if num <= 1:
		return n
	else: 
		return fibonacci(num-1) + fibonacci(num-2)

#iterative solution which is more similar to how a human would create a fibonacci sequence
def fibonacci2(num):
	fibonacci_sequence = [0,1]
	for i in range(2, num + 1):
		new_number = fibonacci_sequence[i-2] + fibonacci_sequence[i-1]
		fibonacci_sequence.append(new_number)
	return fibonacci_sequence[n]


if sys.argv[1] == str(1):
	print(fibonacci(sys.argv[2]))

if sys.argv[1] == str(2):
	print(fibonacci2(sys.argv[2]))

