import time
from bs4 import BeautifulSoup
import requests
import pyautogui as pg
import mouse
url = "https://ums.mu.edu.lb/Student/pickSection.php?semester_idsemester=31&course_idcourse=NjYxMTg3VlRkamhPZmtGQ3Q5cTJWMEU5eG1xazEzZm0yZzM="
#To get the request of the HTML file of any url
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print(soup.prettify())


for i in range(500):
    # links=soup.find_all('select')
    # print(links)
    print(i)
    time.sleep(2)
    pg.press('F5')
    time.sleep(2)
    pg.click(500,210,button='left')
