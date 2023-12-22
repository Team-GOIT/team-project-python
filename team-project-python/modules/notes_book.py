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

        return "There is no note found with this title"

    def search_notes(self, query):
        query_lower = query.lower()
        output = "\n".join(str(note) for note in self.notes if query_lower in str(note).lower())

        if len(output) > 0:
            return "Found notes:\n\n" + output
        else:
            return "No records found with these parameters."

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

        all_notes_template = "All notes:\n\n" + "\n\n".join(map(str, self.notes))
        return all_notes_template

    def add_tag(self, note_title, tag):
        matching_notes = [note for note in self.notes if note.title == note_title]

        if len(matching_notes):
            matching_notes[0].tags.append(tag)
            return f"New tag was added to '{note_title}'"
        else:
            return f"Failed to add new tags for '{note_title}'. Are you sure it exists?"


    def delete_tag(self, note_title, tag):
        matching_notes = [note for note in self.notes if note.title == note_title]

        if matching_notes:
            if tag in matching_notes[0].tags:
                print('removing', matching_notes[0].tags)
                matching_notes[0].tags.remove(tag)
                print('after', matching_notes[0].tags)
                return f"Tag '{tag}' was deleted from '{note_title}'"
            else:
                return f"Tag '{tag}' not found in '{note_title}'"
        else:
            return f"Failed to delete tag for '{note_title}'. Are you sure it exists?"

    def search_notes_by_tags(self, tags):
        matching_notes = [note for note in self.notes if any(tag in note.tags for tag in tags)]

        if matching_notes:
            output = "\n".join(str(note) for note in matching_notes)
            return f"Found notes with tags {tags}:\n\n{output}"
        else:
            return f"No notes found with tags {tags}"
