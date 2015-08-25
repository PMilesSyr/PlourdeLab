import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.test
datasample = db.datasample

db.datasample.insert({"Mon", "Tues", "wed", "Thurs", "Fri", "Sat", "Sun"})

