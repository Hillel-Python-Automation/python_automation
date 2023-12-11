import pytest
from lesson_18.app.calc import Calculator


@pytest.fixture()
def calc():
    calc = Calculator()
    print('lesson_19', id(calc))
    return calc
