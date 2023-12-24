import pytest
import python_automation.lesson_19.home_work.ValentynVildiaiev.tests.crud_tests.test_crud_notes_vv


def test_adding_new_note_err(note_app):
    with pytest.raises(TypeError):
        assert note_app.add_note()


def test_get_note_err(note_app):
    assert note_app.get_note(9) == 'Index out of range'


def test_update_note_err(note_app):
    assert note_app.edit_note(43, 'Something') == 'Index out of range'


def test_delete_note_err(note_app):
    assert note_app.delete_note(19) == 'Index out of range'
