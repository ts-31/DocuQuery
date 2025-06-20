# db/mongo.py
from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGO_URI"))
db = client["docuquery"]
documents_collection = db["documents"]
