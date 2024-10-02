import os
from pymongo import MongoClient

mongo_uri = os.getenv("MONGO_URI", "")
client = MongoClient(mongo_uri)

db = client.database_01

collection_name = db["cities"]
