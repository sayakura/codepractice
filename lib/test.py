from kura_pearson_correlation import pearson_correlation
from recommendations import critics
def get_score(person,other):
	prefs = critics
	x = [prefs[person][x] for x in [x for x in prefs[person] if x in  prefs[other]]]
	y = [prefs[other][y] for y in [y for y in prefs[other] if y in  prefs[person]]]
	return [x, y]

def topMatches(pref, person, n=5):
	scores = [(pearson_correlation(get_score(person,other)[0],get_score(person,other)[1]), other) for other in pref if person != other]
	scores.sort()
	scores.reverse()
	return scores[0:n]
print(topMatches(critics, "Toby",n=3))
