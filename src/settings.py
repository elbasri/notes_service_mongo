import os

def get_mongo_uri():
    return os.getenv('MONGO_URI', 'mongodb://localhost:27017')

def get_database_name():
    return os.getenv('DATABASE_NAME', 'notes_service_mongo')