from bson import ObjectId
from flask import Flask, render_template, url_for, request, redirect
import json
from pymongo import MongoClient
url="mongodb://localhost:27017/"
client = MongoClient(url)
db=client.MyDB
#https://hevodata.com/learn/json-to-mongodb-python/#Inserting_Data_from_JSON_to_MongoDB_Python
#Convert from MongoDB into JSON
#we use mongo to save data locally and make the machine faster
collection=db.Test

class MyFlaskApp(Flask):
    def __init__(self, *args, **kwargs):
        #we use json to send the mongo data to the js to put it in the charts since js understand json
        d = list(collection.find())
        super().__init__(*args, **kwargs)
        with open('output.json', 'w') as outfile:
            json.dump(d, outfile, default=str, indent=4)

app = MyFlaskApp(__name__)

@app.route('/')
def index():
    with open('output.json') as file:
        file_data = json.load(file)
    return render_template("index.html",data=file_data,count=len(file_data))
@app.route('/output')
def out():
    with open('output.json') as file:
        file_data = json.load(file)
    return file_data
if __name__ == '__main__':
    app.run(debug=True)