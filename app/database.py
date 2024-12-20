from pymongo import mongo_client
import pymongo
from api.app.config import settings

client = mongo_client.MongoClient(settings.DATABASE_URL)
print("Connect to MongoDB...")

db = client[settings.MONGO_DB]
User = db.users

User.create_index([("email", pymongo.ASCENDING)], unique=True)
