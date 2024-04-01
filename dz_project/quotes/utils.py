from pymongo import MongoClient


def get_mongodb():

    client = MongoClient('localhost:27017')

    db = client.DZ_10

    return db

