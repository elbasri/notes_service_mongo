from src.notes_service import NotesService

def test_notes_service_initialization():
    service = NotesService()
    assert isinstance(service, NotesService)