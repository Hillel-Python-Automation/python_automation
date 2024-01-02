import pytest

from lesson_18.app.calc import Calculator
from lesson_19.home_work.app.notes_app import NotesApp


@pytest.fixture()
def init_calc():
    yield Calculator()


@pytest.fixture()
def notes_app():
    yield NotesApp()

@pytest.fixture()
def notes_inst():
    return NotesApp()

@pytest.fixture()
def impossible_index(notes_inst):
    list_of_notes = notes_inst.get_all_notes()
    impossible_index = len(list_of_notes)
    return impossible_index

