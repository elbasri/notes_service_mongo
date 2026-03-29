# Import necessary libraries
from flask import Flask, request, jsonify
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)
    client = MongoClient('mongodb://localhost:27017/')
    db = client['notes_db']
    notes_collection = db['notes']

    @app.route('/api/notes', methods=['POST'])
    def create_note():
        note_data = request.json
        result = notes_collection.insert_one(note_data)
        return jsonify({'id': str(result.inserted_id)}), 201

    @app.route('/api/notes', methods=['GET'])
    def get_notes():
        notes = list(notes_collection.find({}, {'_id': 0}))
        return jsonify(notes)

    @app.route('/api/notes/<note_id>', methods=['GET'])
    def get_note(note_id):
        note = notes_collection.find_one({'_id': note_id}, {'_id': 0})
        if note:
            return jsonify(note)
        else:
            return jsonify({'error': 'Note not found'}), 404

    @app.route('/api/notes/<note_id>', methods=['DELETE'])
    def delete_note(note_id):
        result = notes_collection.delete_one({'_id': note_id})
        if result.deleted_count == 1:
            return jsonify({'message': 'Note deleted'})
        else:
            return jsonify({'error': 'Note not found'}), 404

    return app
