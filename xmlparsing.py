import xml.etree.ElementTree as ET
import urllib2

url = raw_input("Enter Location: ")
print "Retrieving "+url
data = ET.fromstring(urllib2.urlopen(url).read())
counts = data.findall("comments/comment/count")
num = 0
print "Count:" + str(len(counts))
for count in counts:
	num += int(count.text)
print num