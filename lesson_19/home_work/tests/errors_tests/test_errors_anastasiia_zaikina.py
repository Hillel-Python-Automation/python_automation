import pytest


def test_error_for_add_note(notes_inst):
    with pytest.raises(TypeError):
        assert notes_inst.add_note()


def test_error_for_get_note(notes_inst, impossible_index):
    assert notes_inst.get_note(impossible_index) == "Index out of range"


def test_error_for_edit_note(notes_inst, impossible_index):
    new_content = 'Mercy'
    assert notes_inst.edit_note(impossible_index, new_content) == "Index out of range"


def test_error_for_delite_note(notes_inst, impossible_index):
    assert notes_inst.delete_note(impossible_index) == "Index out of range"
