from flask import Blueprint, request, jsonify
from src.services.note_service import NoteService
from src.repositories.note_repository import NoteRepository

def create_note_service():
    repository = NoteRepository()
    return NoteService(repository)

note_bp = Blueprint('notes', __name__)
note_service = create_note_service()

@note_bp.route('/notes', methods=['POST'])
def create_note():
    data = request.json
    title = data.get('title')
    content = data.get('content')
    tags = data.get('tags', [])

    note = note_service.create_note(title, content, tags)
    return jsonify(note), 201
