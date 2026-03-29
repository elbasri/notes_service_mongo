from repositories.note_repository import NoteRepository

class NoteService:
    def __init__(self, repository):
        self.repository = repository

    def create_note(self, title, content, tags=None):
        if not title or not content:
            raise ValueError('Title and content are required')
        if tags is None:
            tags = []
        normalized_tags = [tag.strip().lower() for tag in tags]
        note_data = {
            'title': title,
            'content': content,
            'tags': normalized_tags
        }
        return self.repository.create(note_data)

    def get_note(self, note_id):
        return self.repository.get_by_id(note_id)

    def update_note(self, note_id, title=None, content=None, tags=None):
        if not note_id:
            raise ValueError('Note ID is required')
        updates = {}
        if title:
            updates['title'] = title
        if content:
            updates['content'] = content
        if tags is not None:
            normalized_tags = [tag.strip().lower() for tag in tags]
            updates['tags'] = normalized_tags
        return self.repository.update(note_id, updates)

    def delete_note(self, note_id):
        if not note_id:
            raise ValueError('Note ID is required')
        return self.repository.delete(note_id)