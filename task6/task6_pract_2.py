import requests
from pymongo import MongoClient
#Create Connection to "Localhost"
url="mongodb://localhost:27017/"
client = MongoClient(url)
db=client["MyDB"]
collection=db["Test"]
print(list(collection.find()))
print(db)
print(client)
