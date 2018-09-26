import urllib
from BeautifulSoup import *

url = raw_input("Enter your web page for scraping: ")
link_number = int(raw_input("Enter the link number: "))
repetitions = int(raw_input("Enter the number of repetitions: "))

names = []

while repetitions > 0:
    links = []
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    for tag in tags:
        links.append(tag.get('href', None))
    names.append(links[link_number])
    url = links[link_number]
    repetitions -= 1

print names
