import pytest
from lesson_18.app.calc import Calculator


@pytest.fixture()
def calculator():
    return Calculator()
