#Uses python3
#runtime is quadratic
#swap based on index values

def swap(a, x, y):
	temp = a[x]
	a[x] = a[y]
	a[y] = temp
	

def swap_sort(a):
	for i in range(0, len(a)):
		min_index = i
		for j in range(i+1, len(a)):
			if a[j] < a[min_index]:
				min_index = j
		swap(a, min_index, i)
	return a
 
print(swap_sort([5,3,8,7,1,9]))
