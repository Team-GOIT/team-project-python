from .note import Note

class NotesBook:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note)
        return f"Note '{title}' was created"

    def search_notes(self, query):
        query_lower = query.lower()
        output = "\n".join(str(note) for note in self.notes if query_lower in str(note).lower())

        if len(output) > 0:
            return "Found notes:\n\n" + output
        else:
            return "No records found with these parameters."

    def edit_note(self, title, new_content):
        matching_notes = [note for note in self.notes if note.title == title]

        if matching_notes:
            matching_notes[0].content = new_content
            return f"Note '{title}' was updated successfully"
        else:
            return f"Failed to update '{title}'. Are you sure it exists?"

    def delete_note(self, title):
        updated_notes = [note for note in self.notes if note.title != title]

        if len(updated_notes) < len(self.notes):
            self.notes = updated_notes
            return f"Note '{title}' was removed"
        else:
            return f"Failed to delete '{title}'. Are you sure it exists?"

    def get_all_notes(self):
        if not self.notes:
            return "There are no entries yet. Create some."
    
        all_notes_template = "All notes:\n" + "\n".join(map(str, self.notes))
        return all_notes_template