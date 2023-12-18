import pytest

NOTE_VALUE = 'Adding a note test errors'
NOTE_ID = 0
EXPECTED_NOTE_VALUE = 'The edited note errors'


def test_create_note_errors(notes_app):
    with pytest.raises(TypeError):
        assert notes_app.add_note()


def test_read_note_errors(notes_app):
    assert "Index out of range" == notes_app.get_note(NOTE_ID)


def test_update_note_errors(notes_app):
    assert "Index out of range" == notes_app.edit_note(NOTE_ID, EXPECTED_NOTE_VALUE)


def test_delete_note_errors(notes_app):
    assert "Index out of range" == notes_app.delete_note(NOTE_ID)
