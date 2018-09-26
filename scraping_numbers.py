import urllib
from BeautifulSoup import *

url = raw_input("Enter your web page for scraping: ")

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')

count = 0
for tag in tags:
    count += int(tag.contents[0])
print count
