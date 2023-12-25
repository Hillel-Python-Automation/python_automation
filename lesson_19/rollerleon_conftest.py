import pytest
from python_automation.lesson_19.app.notes_app import NotesApp

@pytest.fixture(scope="module")
def notes_app_instance():
    return NotesApp()
