from pymongo import MongoClient
import json
#Create new database
url="mongodb://localhost:27017/"
client = MongoClient(url)
db=client.MyDB
collection=db.Test2
#print the json file
with open('output.json') as file:
    file_data = json.load(file)

collection.insert_many(file_data)
print(file_data)