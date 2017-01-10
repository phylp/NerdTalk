# Uses python3
# Stress test of max_pairwise solutions

import random

def naive(a):
	largest_product = 0
	for i in range(0, len(a)):
		for j in range(0, len(a)):
			if (i != j) and (largest_product < a[i] * a[j]):
				largest_product = a[i]* a[j]
	return largest_product


def simple(a):
	sorted_array = sorted(a)
	length = len(sorted_array)
	return sorted_array[length - 1] * sorted_array[length - 2]

def manual(a):
	max_index1 = -1
	for i in range(0, len(a)):
		if max_index1	 == -1 or a[i] > a[max_index1]:
			max_index1 = i

	max_index2 = -1
	for j in range(0, len(a)):
		if (j != max_index1) and ((max_index2 == -1) or (a[j] > a[max_index2])):
		  max_index2 = j
 
	max_product = a[max_index1] * a[max_index2]
	return max_product

def generate_array():
	test_array = []
	for i in range(6):
		test_array.append(random.randint(1,10))
	return test_array

matching = True

while matching:
	arr = generate_array()	
	print(arr)

	if simple(arr) == manual(arr) and simple(arr) == naive(arr) and manual(arr) == naive(arr):
		print('OK')
	else: 
		print('FAILED')
		matching = False 


