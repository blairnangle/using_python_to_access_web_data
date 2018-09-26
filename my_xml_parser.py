import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_192734.xml'

url = serviceurl + urllib.urlencode({'sensor':'false',})

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
print data
tree = ET.fromstring(data)

results = tree.findall('comments/comment')

countList = []

for result in results:
    countList.append(int(result.find('count').text))

count = 0

for x in countList:
    count += x

print count



