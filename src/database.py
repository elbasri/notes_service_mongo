from pymongo import MongoClient
from config import DATABASE_URI
def get_db():
    client = MongoClient(DATABASE_URI)
    return client['notes_service']