import pytest
from python_automation.lesson_19.rollerleon_conftest import notes_app_instance
def test_read_note_out_of_range(notes_app_instance):
    result = notes_app_instance.get_note(99)
    assert result == "Index out of range"

def test_update_note_out_of_range(notes_app_instance):
    result = notes_app_instance.edit_note(99, "Updated Note")
    assert result == "Index out of range"

def test_delete_note_out_of_range(notes_app_instance):
    result = notes_app_instance.delete_note(99)
    assert result == "Index out of range"
