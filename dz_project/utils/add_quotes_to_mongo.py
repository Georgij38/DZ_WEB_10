import json
from bson.objectid import ObjectId
from pymongo import MongoClient


#ri = "mongodb+srv://user:567234@cluster0.qpllrc8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


client = MongoClient('mongodb://localhost')

db = client.DZ_10

# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

with open('quotes.json','r', encoding='utf-8') as fb:
    quotes = json.load(fb)

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
        })