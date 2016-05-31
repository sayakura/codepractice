import urllib2
data = urllib2.urlopen("http://www.google.com")
print(data).info()