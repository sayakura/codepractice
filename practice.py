import urllib
import re
import matplotlib.pyplot as plt
import pandas as pd
link = raw_input("What's the url?")

if re.search("^http",link):
	counts = dict()
	data = urllib.urlopen(link)
	for line in data:
		words = line.split()
		for word in words:
			counts[word] = counts.get(word, 0) + 1

	s = pd.Series(counts)
	#s.plot(kind='bar',rot=0)
	#plt.show()
	print(s.value_counts)
else:
	print("URL was wrong!")
