from src.notes_repository import NotesRepository

def test_notes_repository_initialization():
    repo = NotesRepository()
    assert isinstance(repo, NotesRepository)