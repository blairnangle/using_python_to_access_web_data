import json
import urllib

url = "http://python-data.dr-chuck.net/comments_192738.json"

uh = urllib.urlopen(url)

dataFromURL = uh.read()
info = json.loads(dataFromURL)

listOfData = info["comments"]

listOfCounts = []
for dict in listOfData:
    countValue = dict["count"]
    listOfCounts.append(countValue)



print sum(listOfCounts)
