import requests
from pymongo import MongoClient
#Create Connection to "Localhost"
url=""
client = MongoClient(url)

#Using [  ]
##Create local 'nobel' database on the fly
db=client["database_name"]
##to get collection from database
collection_var=db['collection_name']

#Using .
##Create local 'nobel' database on the fly
db=client.nobel
##to get collection from database
collection_var=db.collection_name

#To count documents in collections
##it will filter the data that will return to us according to the following inputs
### in the 1st one the gender must be female in the
### $in means one of them 2nd the diedCount must be in Lebanon or france
### $ne means not equals in the 3rd the age must be not equal to 32 or 42
filter={'gender' : 'female','diedCountry':{'$in':['Lebanon','France']},'age':{'$ne':[42,32]}}
#To count documents in collections
n_prizes = db.prizes.count_documents(filter)
n_laureates = db.laureates.count_documents(filter)
##Find one document to inspect
doc = db.prizes.find_one(filter)
##Get the prize collection
prize = db.prizes.find_one()
##to print the list of the collections
print(prize.keys())
#count = ____.____.____(____)
#print(count)
#