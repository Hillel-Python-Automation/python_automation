def test_add_new_note(note_app):
    basic_count = len(note_app.get_all_notes())
    note_app.add_note("Note added successfully")
    new_note_count = len(note_app.get_all_notes())
    assert new_note_count == basic_count + 1


def test_read_added_note(note_app):
    note_app.add_note("Note 1")
    note_app.add_note("Note 2")
    assert note_app.get_note(0) == "Note 1"
    assert note_app.get_note(1) == "Note 2"


def test_update_note(note_app):
    note_app.add_note("Note 3")
    assert note_app.edit_note(0, "Updated Note") == "Note edited successfully"


def test_delete_note(note_app):
    note_app.add_note("Note 1")
    assert note_app.delete_note(0) == "Note is deleted successfully"
