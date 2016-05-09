
def loadMoviesLens():
	movies = {}
	for line in open('u.item'):
		(id, title) = line.split('|')[0:2]
		movies[id] = title
	prefs = {}
	for line in open('u.data'):
		(user,movieid,rating,ts) = line.split('\t')
		prefs.setdefault(user, {})
		prefs[user][movies[movieid]] = float(rating)
	return prefs
prefs = loadMoviesLens()
print prefs['6']