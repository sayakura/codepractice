from recommendations import critics
from auto_machine import supermachine

def getRecommendations(prefs,person):
   totals={}
   simSums={}
   for other in prefs:
    	if other == person: continue
    	sim= supermachine(person,other)
    	if sim<=0: continue
    	for item in prefs[other]:
    		if item not in prefs[person] or prefs[person][item]==0:
    			totals.setdefault(item,0)
    			totals[item]+=prefs[other][item]*sim
    			simSums.setdefault(item,0)
    			simSums[item]+=sim
	rankings=[(total/simSums[item],item) for item,total in totals.items()]
	rankings.sort( )
	rankings.reverse( )
	return rankings

print getRecommendations(critics, "Claudia Puig")