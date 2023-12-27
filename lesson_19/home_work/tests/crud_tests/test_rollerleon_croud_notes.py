import pytest
from python_automation.lesson_19.rollerleon_conftest import notes_app_instance
def test_create_note(notes_app_instance):
    result = notes_app_instance.add_note("Test Note")
    assert result == "Note added successfully"

def test_read_note(notes_app_instance):
    notes_app_instance.add_note("Test Note")
    result = notes_app_instance.get_note(0)
    assert result == "Test Note"

def test_update_note(notes_app_instance):
    notes_app_instance.add_note("Test Note")
    result = notes_app_instance.edit_note(0, "Updated Note")
    assert result == "Note edited successfully"

def test_delete_note(notes_app_instance):
    notes_app_instance.add_note("Test Note")
    result = notes_app_instance.delete_note(0)
    assert result == "Note is deleted successfully"
