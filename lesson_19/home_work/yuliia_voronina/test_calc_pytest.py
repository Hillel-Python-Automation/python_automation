import pytest
from lesson_18.app.calc import Calculator


@pytest.fixture
def calculator_instance():
    return Calculator()


# addiction
@pytest.mark.parametrize(
    "a, b, expected",
    [(0, 0, 0),
     (-5, 5, 0),
     (-12, -88, -100)]
)
def test_addition(calculator_instance, a, b, expected):
    result = calculator_instance.add(a, b)
    assert result == expected


# square_root
@pytest.mark.parametrize(
    "a, expected",
    [(121, 11),
     (16, 4),
     (10000, 100)]
)
def test_square_root(calculator_instance, a, expected):
    result = calculator_instance.square_root(a)
    assert result == expected


# division
@pytest.mark.parametrize(
    "a, b, expected",
    [(6, -2, -3),
     (10000, 1000, 10),
     (5, 2.5, 2)]
)
def test_division(calculator_instance, a, b, expected):
    result = calculator_instance.div(a, b)
    assert result == expected


# mult
@pytest.mark.parametrize(
    "a, b, expected",
    [(5, 3, 15),
     (-1.5, -1.5, 6.25),
     (0, 0, 0)]
)
def test_multiplication(calculator_instance, a, b, expected):
    result = calculator_instance.mult(a, b)
    assert result == expected


# power
@pytest.mark.parametrize(
    "a, b, expected",
    [(2, 3, 8),
     (4, -2, 0.0625),
     (878, 0, 1)]
)
def test_power(calculator_instance, a, b, expected):
    result = calculator_instance.power(a, b)
    assert result == expected


# subtract
@pytest.mark.parametrize(
    "a, b, expected",
    [(8, -3, 11),
     (-4, -4, 0),
     (121, -9, 130)]
)
def test_subtract(calculator_instance, a, b, expected):
    result = calculator_instance.substract(a, b)
    assert result == expected

