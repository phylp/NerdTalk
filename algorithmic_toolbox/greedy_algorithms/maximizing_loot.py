# Uses python3
# This is an implementation of a fractional knapsack. 
# Safe move: take as much of the greatest value and repeat process until the weight of the knapsack is maximized

import sys

def get_optimal_value(capacity, weights, values):
	value = 0
	for i in range(0, len(weights)):
		if capacity == 0:
			return value
		best_value = 0
		best_index = 0
		for j in range(0, len(weights)):
			if (weights[j]) > 0 and (values[j]/weights[j] > best_value):
				best_value = values[j]/weights[j]
				best_index = j
		amount = min(capacity, weights[best_index])
		weights[best_index] -= amount
		value += (best_value * amount)
		capacity -= amount    
	return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))