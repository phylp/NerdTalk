# Uses python3
import sys
import math

def binary_search(a, x):
    low = 0 
    high = len(a)
    while high > low:
        mid = math.floor((low+high)/2)
        if a[mid] > x:
            high = mid -1
        elif a[mid] < x:
            low = mid + 1
        else: 
            return mid
    return -1
