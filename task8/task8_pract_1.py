from bson import ObjectId
from flask import Flask, render_template, url_for, request, redirect
import json
from pymongo import MongoClient

url="mongodb://localhost:27017/"
client = MongoClient(url)
db=client.MyDB
#https://hevodata.com/learn/json-to-mongodb-python/#Inserting_Data_from_JSON_to_MongoDB_Python
#Convert from MongoDB into JSON
collection=db.Test
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        task_content=request.form['content']
    else:
        data=list(collection.find())
        return render_template("index.html",data=data,count=len(data))
@app.route('/delete/<id>')
def delete(id):
    obj_id=ObjectId(id)
    #d=collection.find_one()
    collection.delete_one({'_id':obj_id})
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)