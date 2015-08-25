import pymongo
from pymongo import MongoClient

import datetime


client = MongoClient()
db = client.test

numval = 5

post = {"author": "Mike",
		"text": "My first blog post!",
		"value": 5,
		"varvalue": numval
		}

posts = db.posts
posts.insert(post)

