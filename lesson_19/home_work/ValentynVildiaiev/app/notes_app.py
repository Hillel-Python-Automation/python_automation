class Note:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return f"Note(content={self.content})"



class NotesApp:
    def __init__(self):
        self.notes_list = []

    def add_note(self, content):
        new_note = Note(content)
        self.notes_list.append(new_note)
        return "Note added successfully"

    def get_note(self, index):
        try:
            return self.notes_list[index].content
        except IndexError:
            return "Index out of range"

    def get_all_notes(self):
        return self.notes_list

    def edit_note(self, index, content):
        try:
            self.notes_list[index].content = content
            return "Note edited successfully"
        except IndexError:
            return "Index out of range"

    def delete_note(self, index):
        try:
            self.notes_list.pop(index)
            return "Note is deleted successfully"
        except IndexError:
            return "Index out of range"
