from pymongo import MongoClient
from flask import Flask, jsonify

app = Flask(__name__)

def check_mongo_connectivity():
    try:
        client = MongoClient('mongodb://localhost:27017/')
        client.admin.command('ping')
        return True
    except Exception as e:
        print(f'MongoDB connectivity check failed: {e}')
        return False

@app.route('/health', methods=['GET'])
def health_check():
    mongo_status = 'UP' if check_mongo_connectivity() else 'DOWN'
    return jsonify({'status': 'OK', 'mongo_status': mongo_status})
