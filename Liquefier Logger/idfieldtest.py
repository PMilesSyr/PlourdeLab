import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.test
data = db.data

data.insert({"_id": ObjectId(1), "title": "Title"})