from recommendations import critics
from kura_pearson_correlation import pearson_correlation

def supermachine(person, other):
	personList = []
	for item in critics[person]:
		if item in critics[other]:
			personList.append(item)

	r = pearson_correlation([critics[person][item] for item in personList], [critics[other][item] for item in personList])
	return r

def get_recommendations(person):
	simSums = {}
	totals = {}
	for other in critics:
		if person == other: continue
		sim = supermachine(person, other)

		for item in critics[other]:
			if item not in critics[person] or critics[person][item] == 0:
				totals.setdefault(item, 0)
				totals[item] += critics[other][item] * sim
				simSums.setdefault(item, 0)
				simSums[item] += sim
	rankings = [(total / simSums[item], item) for item, total in totals.items()]
	rankings.sort()
	rankings.reverse()
	return rankings

print get_recommendations("Toby")
