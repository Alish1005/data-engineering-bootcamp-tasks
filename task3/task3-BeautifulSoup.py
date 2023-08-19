
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

print('------------------------EX 2-------------------------------')
url = "https://realpython.github.io/fake-jobs/"
#To get the request of the HTML file of any url
req = requests.get(url)
#print all the HTML code
print(req.text)
soup = BeautifulSoup(req.content, "html.parser")
#get the HTML code for a div that have id ='ResultsContainer'
results = soup.find(id="ResultsContainer")

#get the title of the url
print(soup.title)
#get all the href links for all <a> command in the webpage
for link in soup.find_all('a'):
    print(link.get('href'));
print(results.prettify())
#find all the divs that have class card-content
job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    print(job_element, end="\n"*2)

    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    #.text to get only the value of the code while without it it will return all the code
         #strip it return the value without the extra spaces that the text print it
    print(title_element)
    print(company_element.text)
    print(location_element.text.strip())
    print()
#it will return an array thet contain elements that have the needed information
python_jobs = results.find_all(
        "h2", string=lambda text: "python" in text.lower()
)
print(python_jobs,len(python_jobs))

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
#without this code it will return an error
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
for job_element2 in python_job_elements:
    title_element = job_element2.find("h2", class_="title")
    company_element = job_element2.find("h3", class_="company")
    location_element = job_element2.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())

for job_element in python_job_elements:
    links = job_element.find_all("a")
    for link in links:
        if link["href"]!='https://www.realpython.com':
            link_url = link["href"]
            print(f"Apply here: {link_url}\n")