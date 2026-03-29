from fastapi import APIRouter, HTTPException
from services.notes_service import create_note
from schemas import Note
router = APIRouter()
@router.post('/notes')
def add_note(note: Note):
    note_id = create_note(note.dict())
    return {'id': str(note_id)}