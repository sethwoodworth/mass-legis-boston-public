from BeautifulSoup import BeautifulSoup
import urllib

url = 'http://www.mass.gov/legis/bills/senate/186/st00/st00593.htm'
response = urllib.urlopen(url)
raw_html = response.read()
soup = BeautifulSoup(raw_html)

print soup.prettify()
