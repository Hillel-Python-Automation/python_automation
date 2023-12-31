import pytest
from python_automation.Lesson_18.app.calc import Calculator

@pytest.fixture
def my_fixture():
    return Calculator

@pytest.fixture(scope='session')
def my_fixture():
    yield
def test_add_tow_numbers(my_fixture):

    assert Calculator.add(None,2, 2) == 4
    assert Calculator.add(None,0, 2) == 2
    assert Calculator.add(None,-1, 1) == 0
    assert Calculator.add(None,0.1, -0.1) == 0

def test_subtract_func(my_fixture):

    assert Calculator.substract(None,4,2) == 2
    assert Calculator.substract(None,0, 0) == 0
    assert Calculator.substract(None,10, 1) == 9
    assert Calculator.substract(None,0.1, 0.1) == 0

def test_division_func(my_fixture):

    with pytest.raises(ZeroDivisionError):
        Calculator.div(None,1, 0)
    assert Calculator.div(None,4,2) == 2
    assert Calculator.div(None,0,1) == 0
    assert Calculator.div(None, 0.25, 0.25) == 1

def test_sqrt_func(my_fixture):

    assert Calculator.square_root(None,4) == 2
    assert Calculator.square_root(None,0) == 0
    assert Calculator.square_root(None,64) == 8
    assert Calculator.square_root(None,1) == 1

def test_mult_func(my_fixture):

    assert Calculator.mult(None, 2,2) == 4
    assert Calculator.mult(None, 0,0) == 0
    assert Calculator.mult(None, 1,0) == 0
    assert Calculator.mult(None, -2, 2) == -4