from bson import ObjectId
from bs4 import BeautifulSoup
import requests
import datetime
import json
from flask import Flask, render_template
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

class MyFlaskApp(Flask):
    def __init__(self, *args, **kwargs):
        #we use json to send the mongo data to the js to put it in the charts since js understand json
        last_75_documents = collection.distinct("date")[-1] - datetime.timedelta(days=75)
        d = list(collection.find(filter={"date": {"$exists": last_75_documents}}))
        super().__init__(*args, **kwargs)
        with open('output.json', 'w') as outfile:
            json.dump(d, outfile, default=str, indent=4)

app = MyFlaskApp(__name__)


def save_xml_mongo(before_now:int=1):
    #print(list(collection.find().sort("date", -1))[0]['date'])
    for i in range(0,before_now):
        before_now_date = date - datetime.timedelta(days=i)
        before_now_date=before_now_date.replace(hour=0,minute=0,second=0,microsecond=0)
        print(before_now_date)
        #Any Error after 75 day turn this to continue
        if not is_date_need_data(before_now_date):
            break
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
            continue
        collection.insert_one({
            "url": i.url,
            "type":i.type,
            "topic":i.topic,
            "date":i.publish_date
        });
        print("save")
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
def top_type():
    last_75_documents = collection.distinct("date")[-1]- datetime.timedelta(days=75)
    types=collection.distinct("type")
    top="None"
    max=0;
    for i in types:
        count=collection.count_documents({"$and":[{"type":i} ,{"date":{"$gte":last_75_documents}}]})
        if max<count:
            max=count
            top=i
    return top
def top_topic():
    last_75_documents = collection.distinct("date")[-1]- datetime.timedelta(days=75)
    types=collection.distinct("topic")
    top="1"
    max=0;
    for i in types:
        count=collection.count_documents({"$and":[{"topic":i} ,{"date":{"$gte":last_75_documents}}]})
        print(i," : ",count);
        if max<count  and i!='None':
            max=count
            top=i
    return top

def nbOfNews(d:datetime):
    return collection.count_documents({"date":d})
def nbOfNews(days:int):
    d=date-datetime.timedelta(days=days)
    n=collection.count_documents({"date":{"$gte":d}})
    return n

def topic_array():
    last_75_documents = collection.distinct("date")[-1]- datetime.timedelta(days=75)
    topics=collection.distinct("topic",filter={"date":{"gte":last_75_documents}})
    print(topics)
    print(len(topics))
    array=[[],[]]
    for i in topics:
        array[0].append(i);
        count=collection.count_documents({"topic":i,"date":{"gte":last_75_documents}})
        array[1].append(count)
    return array
def type_array():
    last_75_documents = collection.distinct("date")[-1]- datetime.timedelta(days=75)
    types=collection.distinct("type",filter={"date":{"gte":last_75_documents}})
    array=[[],[]]
    for i in types:
        array[0].append(i);
        count=collection.count_documents({"type":i,"date":{"$gte":last_75_documents}})
        array[1].append(count)
    return array
def date_array():
    last_75_documents = collection.distinct("date")[-1]
    array=[[],[]]
    for i in range(75,-1,-1):
        if i<75 :
            d=(collection.distinct("date")[-1]- datetime.timedelta(days=i));
            array[0].append(d);
            count=collection.count_documents({"date":{"$eq":d}})
            array[1].append(count)
    return array
#Routes
@app.route('/')
def index():
    data = list(collection.find())
    return render_template("main.html",top_topic=top_topic(),top_type=top_type(),nb=nbOfNews(75),arr_topic=topic_array(),arr_type=type_array(),arr_date=date_array())
@app.route('/a')
def a():
    with open("a.json", "w") as json_file:
        json.dump(list(collection.find()), json_file, default=str, indent=4)
    with open('a.json') as file:
        file_data = json.load(file)
    return file_data
@app.route('/data')
def data():
    with open('output.json') as file:
        file_data = json.load(file)
    return file_data

if __name__ == '__main__':
    app.run(debug=True)
