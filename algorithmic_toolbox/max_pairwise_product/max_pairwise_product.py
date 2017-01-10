# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

sorted_array = sorted(a)
length = len(sorted_array)
result = sorted_array[length - 1] * sorted_array[length - 2]
	
print(result) 
