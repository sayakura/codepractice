from BeautifulSoup import *
import re
import urllib2
url = "http://www.ubuntu.com/desktop"
html = urllib2.urlopen(url).read()


soup = BeautifulSoup(


	html)

tags = soup('p')

for tag in tags:
	print tag.string