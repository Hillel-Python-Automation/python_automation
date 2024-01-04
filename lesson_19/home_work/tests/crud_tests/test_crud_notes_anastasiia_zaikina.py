value_for_notes = 'Hello my friend'
value_for_update = 'By my friend'


def test_add_note(notes_inst):
    new_note = notes_inst.add_note(value_for_notes)
    assert new_note == "Note added successfully"


def test_get_note(notes_inst):
    notes_inst.add_note(value_for_notes)
    assert notes_inst.get_note(-1) == value_for_notes


def test_edit_note(notes_inst):
    notes_inst.add_note(value_for_notes)
    edit_note = notes_inst.edit_note(-1, value_for_update)
    assert edit_note == "Note edited successfully"


def test_delete_note(notes_inst):
    notes_inst.add_note(value_for_notes)
    assert notes_inst.delete_note(-1) == "Note is deleted successfully"
