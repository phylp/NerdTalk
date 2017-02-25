# Uses python3
import sys
from math import floor

def mergeit(left, right):
    result = []
    leftIdx = 0
    rightIdx = 0
    while leftIdx < len(left) and rightIdx < len(right):
        if left[leftIdx] <= right[rightIdx]:
            result.append(left[leftIdx])
            leftIdx += 1
        else: 
            result.append(right[rightIdx])
            rightIdx += 1
    if leftIdx < len(left):
        result.extend(left[leftIdx:])
    if rightIdx < len(right):
        result.extend(right[rightIdx:])
    return result

def mergeSort(a):
    if len(a) <= 1:
        return a
    mid = floor(len(a)/2)
    b = mergeSort(a[:mid])
    c = mergeSort(a[mid:])
    return mergeit(b,c)

# print(mergeSort([65,1,3,6,8,7]))
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    for i in (mergeSort(a)):
        print(i)

