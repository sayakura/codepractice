from math import sqrt 
from recommendations import critics

def get_distance(person, other):
	sim = {}
	for item in critics[person]:
		if item in critics[other]:
			sim[item] = 1

	if len(item) == 0 : return 0
	sum_of_squares = sum([pow(critics[person][item] -critics[other][item], 2) for item in critics[other]])
	return 1/(1+sum_of_squares)
print get_distance("Lisa Rose","Gene Seymour")