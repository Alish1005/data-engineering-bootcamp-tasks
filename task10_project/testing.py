from bson import ObjectId
from bs4 import BeautifulSoup
import requests
import datetime
import json
from pymongo import MongoClient
from News import News

date=datetime.datetime.now()
date=date.replace(hour=0,minute=0,second=0,microsecond=0)
url="mongodb://localhost:27017/"
client = MongoClient(url)
db=client.projects
#https://hevodata.com/learn/json-to-mongodb-python/#Inserting_Data_from_JSON_to_MongoDB_Python
#Convert from MongoDB into JSON
#we use mongo to save data locally and make the machine faster
collection=db.aljazeera


def __init__(self, *args, **kwargs):
        #we use json to send the mongo data to the js to put it in the charts since js understand json
        d = list(collection.find())
        super().__init__(*args, **kwargs)
        with open('output.json', 'w') as outfile:
            json.dump(d, outfile, default=str, indent=4)

def save_xml_mongo(before_now:int=1):
    #print(list(collection.find().sort("date", -1))[0]['date'])
    for i in range(0,before_now):
        before_now_date = date - datetime.timedelta(days=i)
        print(before_now_date)
        before_now_date=before_now_date.replace(hour=0,minute=0,second=0,microsecond=0)
        print(before_now_date)
        if not is_date_need_data(before_now_date):
            continue
        xml_url = f"https://www.aljazeera.com/sitemap.xml?yyyy={before_now_date.year}&mm={before_now_date.month:02d}&dd={before_now_date.day:02d}"
        print(">>>>>>>",xml_url,"<<<<<<<")
        req = requests.get(xml_url)  # get the request from the url
        soup = BeautifulSoup(req.text, "xml")  # get the soup of the site
        links = soup.find_all('url')  # seaching
        for link in links :
            url_news=link.loc.text
            print(url_news)
            url_news_split=url_news.split("/")
            type=url_news_split[3]
            print(type)
            req_html = requests.get(url_news)  # get the request from the url
            soup_html = BeautifulSoup(req_html.text, "html.parser")  # get the soup of the site
            if type=='program':
                sub_title = list(soup_html.find('span', class_="program__page__source"))  # seaching
                topic=sub_title[0].text
            else:
                #print(soup_html.text)
                sub_title = soup_html.find_all('div',class_="topics")# seaching
                for s in sub_title:
                    if len(s.find_all('a'))>1:
                        topic=s.find_all('a')[1].text
                        print(topic)
                    else:
                        topic="None"
                        print("None")
            News(url_news,type,topic,before_now_date)

    for i in News.all:
        if collection.count_documents({'url': i.url})>0:
            print('Done')
            break
        collection.insert_one({
            "url": i.url,
            "type":i.type,
            "topic":i.topic,
            "date":i.publish_date
        });

def is_date_need_data(data_date:datetime):
    url = f"https://www.aljazeera.com/sitemap.xml?yyyy={data_date.year}&mm={data_date.month:02d}&dd={data_date.day:02d}"
    req = requests.get(url)  # get the request from the url
    soup = BeautifulSoup(req.text, "xml")  # get the soup of the site
    links = soup.find_all('url')
    l=len(links)-1
    n=collection.count_documents({'date':data_date})
    if n<l:
        return True
    else:
        return False
def nbNews_date():
    l=list()
    for i in range(75,-1,0):
        print(i)
def nbOfNews(d:datetime):
    return collection.count_documents({"date":d})
def nbOfNews(days):
    n=0
    for i in range(0,days):
        d=date-datetime.timedelta(days=i)
        n=n+collection.count_documents({"date":d})
    return n
#Update to Correct the topic data
def updates1():
    for i in list(collection.find()):
        url_news = i['url']
        print(url_news)
        req_html = requests.get(url_news)  # get the request from the url
        soup_html = BeautifulSoup(req_html.text, "html.parser")  # get the soup of the site
        # print(soup_html.text)
        sub_title = soup_html.find_all('div', class_="topics")  # seaching
        for s in sub_title:
            if len(s.find_all('a')) > 1:
                continue
            else:
                print("None")
                collection.update_one({"_id":ObjectId(i['_id'])},{"$set":{'topic':'None'}})
def top_type():
    types=collection.distinct("type")
    print(types)
    top="None"
    max=0;
    for i in types:
        count=collection.count_documents({"type":i})
        print(count)
        if max<count:
            max=count
            top=i
    return top
def top_topic():
    topics=collection.distinct("topic")
    print(topics)
    print(len(topics))
    top="None"
    max=-100;
    for i in topics:
        count=collection.count_documents({"topic":i})
        print(count)
        if count>max and i!='None':
            max=count
            top=i
    return top

print(len(collection.distinct('topic',{'type':'program'})))

#print(is_date_need_data(datetime.datetime(2023, 8, 23)))
