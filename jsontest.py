import json
import urllib2

url = "http://python-data.dr-chuck.net/comments_269042.json"

data = urllib2.urlopen(url).read()

dict_data = json.loads(data)

num = 0
for count in dict_data['comments']:
	num += int(count['count'])
print num