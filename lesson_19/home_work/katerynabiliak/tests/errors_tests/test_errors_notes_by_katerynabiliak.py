import pytest
def test_get_note_error(notes_app):
    assert notes_app.get_note(0) == "Index out of range"

def test_add_note_error(notes_app):
    with pytest.raises(TypeError):
        assert notes_app.add_note()

def test_update_note_error(notes_app):
    assert notes_app.edit_note(1, "example") == "Index out of range"

def test_delete_note_error(notes_app):
    assert notes_app.delete_note(1) == "Index out of range"