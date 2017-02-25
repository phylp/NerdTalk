#key lemma of this problem is that the last digit of each number in the sequence repeats in cycles of 60
#so, the last digit of fib 120 = last digit of fib 0, and the last digit of fib 5 = last digit of fib 185, etc.

import sys

def find_index(num):
    if num <= 60:
        return num
    else:
        while num > 60:
            num -= 60
    return num
        
def get_fibonacci_last_digit(n):
    sequence = [0,1]
    for i in range(2, 61):
        new_number = sequence[i-1] + sequence[i-2] 
        sequence.append(new_number%10)
    target_index = find_index(n)
    return sequence[target_index]

arg = int(sys.argv[1])
print(get_fibonacci_last_digit(arg))


#naive solution
# def get_fibonacci_last_digit_naive(n):
#     if n <= 1:
#         return n
#     previous = 0
#     current  = 1
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#     return current % 10
# 	