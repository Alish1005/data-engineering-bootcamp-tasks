import json

import pymongo
import json
from pymongo import MongoClient


url="mongodb://localhost:27017/"
client = MongoClient(url)
db=client.MyDB
#https://hevodata.com/learn/json-to-mongodb-python/#Inserting_Data_from_JSON_to_MongoDB_Python
#Convert from MongoDB into JSON
collection=db.Test
d=list(collection.find())
with open('output.json','w') as outfile:
     json.dump(d,outfile,default=str, indent=4)
#Convert from json into mongodb
with open('output.json') as file:
    file_data = json.load(file)
#to insert data from json to mongo
#collection.insert_one(file_data)
#collection.insert_many(file_data)
print(file_data)