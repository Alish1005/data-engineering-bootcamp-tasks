from bs4 import BeautifulSoup
#to get data online
import requests
import datetime
# year=input("enter the year:")
# month=int(input("enter the month:"))
# day=int(input("enter the day:"))
# if month<9:
#     month=str(month)
#     month="0"+month
# else:
#     month = str(month)
# if day<9:
#     day=str(day)
#     day = "0" + day
# else:
#     day = str(day)
# url = f"https://www.aljazeera.com/sitemap.xml?yyyy={year}&mm={month}&dd={day}"
# req = requests.get(url) #get the request from the url
# soup = BeautifulSoup(req.text, "xml") #get the soup of the site
# links=soup.find_all('url') #seaching
# for link in links:
#     print(link.loc.text)
# print(len(links))

# url2=input("enter url:")
# req2 = requests.get(url2)
# if str(req2)=="<Response [200]>":
#     soup = BeautifulSoup(req2.text, "html.parser")
#     links2=soup.find_all('div',class_='date-simple')
#     for link in links2:
#         print(link.span.text)
# else:
#     print("wrong url")

#ex3
#Show all the links and the count of the last 75 day before
year=input("enter the year:")
month=int(input("enter the month:"))
day=int(input("enter the day:"))
last=int(input("enter before how much days:"))
if month<9:
    month=str(month)
    month="0"+month
else:
    month = str(month)
if day<9:
    day=str(day)
    day = "0" + day
else:
    day = str(day)
news_number=0
for i in range(0,last):
    time=datetime.datetime(int(year),int(month),int(day))
    days_to_subtract = datetime.timedelta(days=i)
    time=time-days_to_subtract;
    url = f"https://www.aljazeera.com/sitemap.xml?yyyy={time.year.real}&mm={time.month.real}&dd={time.day.real}"
    print(f'>>>>>>>>>>>>{url}<<<<<<<<<<<')
    req = requests.get(url) #get the request from the url
    soup = BeautifulSoup(req.text, "xml") #get the soup of the site
    links=soup.find_all('url') #seaching
    news_number+=len(links)
    for link in links:
        print(link.loc.text)
print(news_number)
