from pymongo import mongo_client
from app.config import settings

client = mongo_client.MongoClient(settings.DATABASE_URL)
print('Connect to MongoDB...')
