from pymongo import MongoClient
from settings import get_mongo_uri, get_database_name
import functools

@functools.lru_cache(maxsize=1)
def get_db_connection():
    client = MongoClient(get_mongo_uri())
    return client[get_database_name()]