import pytest

from lesson_18.app.calc import Calculator
from lesson_19.home_work.app.notes_app import NotesApp


@pytest.fixture(scope='module')
def my_calc():
    return Calculator()


@pytest.fixture()
def note_app():
    return NotesApp()
