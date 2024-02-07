first_row = "example row"

def test_create(notes_app):
    res1 = notes_app.add_note("test note 1")
    res2 = notes_app.add_note("test note 2")
    res3 = notes_app.add_note(first_row)

    assert len(notes_app.notes_list) == 3
    assert notes_app.notes_list[0].content == "test note 1"
    assert notes_app.notes_list[1].content == "test note 2"
    assert notes_app.notes_list[2].content == first_row
    assert res1 == "Note added successfully"
    assert res2 == "Note added successfully"
    assert res3 == "Note added successfully"


def test_read(notes_app):
    notes_app.add_note("row 1")
    notes_app.add_note("row 2")
    assert notes_app.get_note(0) == "row 1"
    assert notes_app.get_note(1) == "row 2"


def test_update(notes_app):
    notes_app.add_note("row 3")
    res = notes_app.edit_note(0, "updated row 3")
    assert res == "Note edited successfully"



def test_delete(notes_app):
    notes_app.add_note("row 1")
    res = notes_app.delete_note(0)
    assert res == "Note is deleted successfully"