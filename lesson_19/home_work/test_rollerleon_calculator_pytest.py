import pytest
from python_automation.lesson_18.app.calc import Calculator

@pytest.fixture
def calculator_instance():
    return Calculator()
# addiction
@pytest.mark.parametrize("a, b, expected", [(3, -2, 1), (4, 5, 9), (7, 3, 10)])
def test_addition(calculator_instance, a, b, expected):
    result = calculator_instance.add(a, b)
    assert result == expected

# square_root
@pytest.mark.parametrize("a, b, expected", [(9, 0, 3), (1, 0, 1), (0, 0, 0)])
def test_square_root(calculator_instance, a, b, expected):
    result = calculator_instance.square_root(a)
    assert result == expected

# division
@pytest.mark.parametrize("a, b, expected", [(6, 2, 3), (-5, 2, -2.5), (-3, -2, 1.5)])
def test_division(calculator_instance, a, b, expected):
    result = calculator_instance.div(a, b)
    assert result == expected

# mult
@pytest.mark.parametrize("a, b, expected", [(1, 3, 3), (-1.5, -2, 3), (3, 0, 0)])
def test_multiplication(calculator_instance, a, b, expected):
    result = calculator_instance.mult(a, b)
    assert result == expected

# power
@pytest.mark.parametrize("a, b, expected", [(3, 3, 27), (4, -2, 0.0625), (4, 0, 1)])
def test_power(calculator_instance, a, b, expected):
    result = calculator_instance.power(a, b)
    assert result == expected

# subtract
@pytest.mark.parametrize("a, b, expected", [(8, 3, 5), (-6, -3, -3), (5, -3, 8)])
def test_substract (calculator_instance, a, b, expected):
    result = calculator_instance.substract(a, b)
    assert result == expected




import pytest
from python_automation.lesson_18.app.calc import Calculator

@pytest.fixture
def calculator_instance():
    return Calculator()

def test_divide_by_zero(calculator_instance):
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        calculator_instance.div(10, 0)

def test_square_root_negative_number(calculator_instance):
    with pytest.raises(ValueError, match="math domain error"):
        calculator_instance.square_root(-9)