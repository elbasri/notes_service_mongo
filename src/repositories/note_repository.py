from pymongo import MongoClient
from bson.objectid import ObjectId

class NoteRepository:
    def __init__(self, db_url):
        self.client = MongoClient(db_url)
        self.db = self.client['notes_service']
        self.collection = self.db['notes']

    def create(self, note):
        result = self.collection.insert_one(note)
        return str(result.inserted_id)

    def list(self):
        notes = self.collection.find()
        return [note for note in notes]

    def get_by_id(self, note_id):
        try:
            note = self.collection.find_one({'_id': ObjectId(note_id)})
            if note is None:
                raise ValueError('Note not found')
            return note
        except (ObjectIdError, ValueError) as e:
            raise ValueError(f'Invalid note ID: {e}') from e

    def delete(self, note_id):
        try:
            result = self.collection.delete_one({'_id': ObjectId(note_id)})
            if result.deleted_count == 0:
                raise ValueError('Note not found')
        except (ObjectIdError, ValueError) as e:
            raise ValueError(f'Invalid note ID: {e}') from e
