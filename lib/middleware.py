from recommendations import critics
def get_score(person,other):
	prefs = critics
	x = [prefs[person][x] for x in [x for x in prefs[person] if x in  prefs[other]]]
	y = [prefs[other][y] for y in [y for y in prefs[other] if y in  prefs[person]]]
	return x, y

print get_score("Lisa Rose", "Toby")[0]