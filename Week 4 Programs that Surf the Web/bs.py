import urllib.request as ur
from bs4 import *

url = input('Enter the url to scrape - ')
# http://www.dr-chuck.com

html = ur.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
# wrapping the whole HTML into a single soup object

tags = soup('a')
# extracts all 'a' tag from the HTML object

for tag in tags:
    print(tag.get('href'), None)
    # each tag is returned as a dictionary of its attributes
