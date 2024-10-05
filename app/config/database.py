import os
from pymongo import MongoClient

mongo_uri = os.getenv("MONGO_URI", "")
client = MongoClient(mongo_uri)

db = client.database_01

cities_collection_name = db["cities"]
countries_collection_name = db["countries"]
