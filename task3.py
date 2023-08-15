
from bs4 import BeautifulSoup
import requests
url = "https://www.tutorialspoint.com/index.htm"
#To get the request of the HTML file of any url
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
#get the title of the url
print(soup.title)
#get all the href links for all <a> command in the webpage
for link in soup.find_all('a'):
    print(link.get('href'));
