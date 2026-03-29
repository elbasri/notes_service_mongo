from database import get_db
from schemas import Note
def create_note(note_data: dict):
    db = get_db()
    notes_collection = db['notes']
    result = notes_collection.insert_one(note_data)
    return result.inserted_id