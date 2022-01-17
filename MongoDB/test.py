import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://Meyr:kbtu2021@cluster0.eexlo.mongodb.net/MeyrDBtest?retryWrites=true&w=majority")

db = cluster["MeyrDBtest"]
collection = db["MeyrColltest"]

post = {"_id": 0, "name": "Meyr", "score": 5}
collection.insert_one(post)

