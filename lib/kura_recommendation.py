from recommendations import critics
from kura_pearson_correlation import pearson_correlation
from middleware import get_score 

def get_recommendation(prefs, person):
	for other in prefs:
		if other == person: continue
		r = pearson_correlation(get_score(person, other)[0], get_score(other, person)[1])
