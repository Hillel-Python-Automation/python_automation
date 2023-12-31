import pytest
from python_automation.Lesson_18.app.calc import Calculator

@pytest.fixture
def my_fixture():
    return Calculator()

def test_add_invalid_type(my_fixture):
    with pytest.raises(TypeError, match='Please use only correct type of values: int or float'):
        my_fixture.add('4', 5)

def test_divide_by_zero(my_fixture):
    with pytest.raises(ZeroDivisionError):
        my_fixture.div(3, 0)

def test_sqrt_negative_number(my_fixture):
    with pytest.raises(ValueError, match='Math domain error'):
        my_fixture.square_root(-64)


