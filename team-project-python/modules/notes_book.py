from .note import Note


class NotesBook:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content, tags):
        note = Note(title, content, tags)
        self.notes.append(note)
        return f"Note '{title}' was created"

    def get_note(self, title):
        for note in self.notes:
            if note.title == title:
                return note

        return None

    def edit_note(self, title, new_content, new_tags):
        matching_notes = [note for note in self.notes if note.title == title]

        if matching_notes:
            matching_notes[0].content = new_content
            matching_notes[0].tags = new_tags
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
            return "There are no notes yet. Create some."

        all_notes_template = "All notes:\n\n" + "\n".join(map(lambda note: note.get_formatted(), self.notes))
        return all_notes_template

    def add_tag(self, note_title, tag):
        matching_notes = [note for note in self.notes if note.title == note_title]

        if len(matching_notes):
            matching_notes[0].tags.append(tag)
            return f"New tag was added to '{note_title}'"
        else:
            return f"There is no note with title: '{note_title}'"

    def delete_tag(self, note_title, tag):
        matching_notes = [note for note in self.notes if note.title == note_title]

        if matching_notes:
            if tag in matching_notes[0].tags:
                matching_notes[0].tags.remove(tag)
                return f"Tag '{tag}' was deleted from '{note_title}'"
            else:
                return f"Tag '{tag}' not found in '{note_title}'"
        else:
            return f"Failed to delete tag for '{note_title}'. Are you sure it exists?"

    def search_notes_by_tags(self, query=None, tags=None):
        matching_notes = self.notes

        if query:
            query_lower = query.lower().strip()
            matching_notes = [
                note for note in matching_notes if query_lower in note.title.lower() or query_lower in note.content.lower()
            ]

        if tags:
            tags_lower = [tag.lower().strip() for tag in tags]
            filtered_by_tags = [
                note for note in matching_notes if any(t in [t.lower().strip() for t in note.tags] for t in tags_lower)
            ]
            matching_notes = sorted(filtered_by_tags, key=lambda note: note.tags)

        if not matching_notes:
            return "No matching notes found."

        return "Matching notes:\n\n" + "\n".join(map(lambda note: note.get_formatted(), matching_notes))