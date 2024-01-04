import pytest
from python_automation.Lesson_18.app.calc import Calculator

@pytest.fixture
def my_fixture():
    return Calculator()

def test_create(my_fixture):
    result = Calculator.add(None, 2, 3)
    assert result == 5

def test_read(my_fixture):

    result = Calculator.substract(None,5, 2)
    assert result == 3

def test_update(my_fixture):
    result = Calculator.mult(None ,3, 4)
    assert result == 12

def test_delete(my_fixture):
    result = Calculator.div(None,10, 2)
    assert result == 5

def test_power(my_fixture):
    result = Calculator.power(None,2, 3)
    assert result == 8

def test_square_root(my_fixture):
    result = Calculator.square_root(None,25)
    assert result == 5
