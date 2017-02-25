# Uses python3
# Given a list of sorted children (represented by their rspective ages), organize the children in the minimum number of groups possible where the age difference between any two children in a given group is at most 1 year
# Safe move: cover the leftmost point (in age) with a unit segment (1 year) and repeat this process

#example input: [5, 5.5, 5.8, 6, 7]
#example output [{youngest: 5, oldest: 6}, {youngest: 7, oldest: 8}]

def group_children(children):
	groups = []
	length = len(children)
	i = 0
	while i <= length:
		age_limit = children[i] + 1	
		groups.append({'youngest':children[i],'oldest': age_limit})
		i += i
		while i <= length and children[i] <= age_limit:
			i += 1
	return groups, len(groups)

print(group_children([5, 5.5, 5.8, 6, 7]))


