#lemma: optimal solution is to use as much as possible the item which has the best value per unit of weight

# while knapsack is not full, 
# choose item i with maximum value (vi/wi)
# place as much of item as possible intop knapsack
# update amount, value, item weight, and weight 
# return knapsack and total value

import math

items = [
	{'w': 4, 'v': 20},
 	{'w': 3, 'v': 18},
 	{'w': 2, 'v': 14} 
]

def knapsack(weight, items):
	sack = [0,0,0]
	value = 0
	for i in range(0, len(items)):
		if weight == 0:
			return sack, value
		#go through, find best value per unit, remove best from items
		best_value = 0
		best_index = 0
		for j in range(0, len(items)):
			if (items[j]['w'] > 0) and ((items[j]['v'])/(items[j]['w']) > best_value):
				best_index = j
				best_value = (items[j]['v'])/(items[j]['w'])
		amount = min(items[best_index]['w'], weight)
		value = value + (amount * best_value)
		items[best_index]['w'] -= amount
		sack[i] = sack[i] + amount 
		weight = weight - amount

	return sack, value


print(knapsack(5, items))



