from pprint import pprint

NOTE_VALUE = 'Adding a note test'
NOTE_ID = 3
EXPECTED_NOTE_VALUE = 'The edited note'


def test_create_note(notes_app):
    number_of_notes = len(notes_app.get_all_notes())
    assert "Note added successfully" == notes_app.add_note(NOTE_VALUE)
    assert len(notes_app.get_all_notes()) == number_of_notes + 1


def test_read_note(notes_app):
    notes_app.add_note(NOTE_VALUE)
    assert notes_app.get_note(-1) == NOTE_VALUE


def test_update_note(notes_app):
    add_notes(notes_app, NOTE_ID)
    notes_app.edit_note(NOTE_ID, EXPECTED_NOTE_VALUE)
    assert EXPECTED_NOTE_VALUE == notes_app.get_note(NOTE_ID)


def test_delete_note(notes_app):
    add_notes(notes_app, NOTE_ID)
    init_state = notes_app.get_all_notes().copy()
    assert "Note is deleted successfully" == notes_app.delete_note(NOTE_ID)
    actual_state = notes_app.get_all_notes()
    assert len(actual_state) == len(init_state) - 1
    print('/n')
    pprint([a.content for a in actual_state])
    pprint([i.content for i in init_state])

    assert actual_state != init_state


def add_notes(notes_app, n):
    for i in range(n + 1):
        notes_app.add_note(f'{NOTE_VALUE} {i}')
