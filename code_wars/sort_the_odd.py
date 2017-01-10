#given an array of integers, return an array with only the odd numbers sorted
# example: [1,5,3,2,7,6] --> [1,3,5,2,7,6]

#phylp solution:
def sort_array(source_array):
    odds = []
    solution = []
    odd_index = 0
    
    for i in range (0, len(source_array)):
        if source_array[i] % 2 != 0:
            odds.append(source_array[i])
            odds = sorted(odds)
            
    for j in range(0, len(source_array)):
        if source_array[j] % 2 == 0:
            solution.append(source_array[j])
        else:
            solution.append(odds[odd_index])
            odd_index += 1
    return solution


#boss solution from MFreidank:
def sort_array(source_array):
    odds = iter(sorted(v for v in source_array if v % 2))
    return [next(odds) if i % 2 else i for i in source_array]