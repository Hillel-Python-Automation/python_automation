import pytest

from lesson_18.app.calc import Calculator
from lesson_19.home_work.app.notes_app import NotesApp


@pytest.fixture()
def init_calc():
    yield Calculator()


@pytest.fixture()
def notes_app():
    yield NotesApp()
