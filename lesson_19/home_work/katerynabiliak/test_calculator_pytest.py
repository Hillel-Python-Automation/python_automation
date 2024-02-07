import sys
import pytest
from lesson_18.app.calc import Calculator


@pytest.fixture()
def calc():
    return Calculator()


@pytest.mark.parametrize('a, b, expected',
                         [
                             (1, 1, 2),
                             (1.5, 1.5, 3),
                             (0.1, 0.1, 0.2),
                             (1000, -1000, 0),
                             (12, 12, 24),
                             (-12, -12, -24),
                             pytest.param(11, 10, 21, marks=pytest.mark.skipif(
                                 sys.platform == 'linux',
                                 reason="The test shouldn't be executed on "
                                        "linux")),
                             pytest.param(12, 12, 24, marks=pytest.mark.skip(
                                 reason="just because")),
                         ]
                         )
def test_add_func(calc, a, b, expected):
    assert calc.add(a, b) == expected


@pytest.mark.parametrize("a, b, expected",
                         [
                             (100, 50, 50),
                             (0.9, 0.8, 0.1),
                             (123, -123, 246),
                             (-100, -100, 0),
                         ]
                         )
def test_subtract_func(calc, a, b, expected):
    actual = round(calc.substract(a, b), 2)
    assert actual == expected


@pytest.mark.parametrize("a, b, expected",
                         [
                             (1, 1, 1),
                             (200, 200, 40000),
                             (0.1, 0.1, 0.01),
                             (-2, 2, -4),
                             (-5, -10, 50),
                         ]
                         )
def test_mult_func(calc, a, b, expected):
    actual = round(calc.mult(a, b), 2)
    assert actual == expected


@pytest.mark.parametrize("a, b, expected",
                         [
                             (10, 5, 2),
                             (-10, -5, 2),
                             (-10, 5, -2),
                             (10, -5, -2),
                             (100.5, 2.1, 47.86),
                         ]
                         )
def test_div_func(calc, a, b, expected):
    actual = round(calc.div(a, b), 2)
    assert actual == expected


@pytest.mark.parametrize("a, expected",
                         [
                             (2, 1.41),
                             (1, 1),
                             (9, 3),
                             (2.2, 1.48),
                         ]
                         )
def test_square_root_func(calc, a, expected):
    actual = round(calc.square_root(a), 2)
    assert actual == expected


@pytest.mark.parametrize("a, b, expected",
                         [
                             (2, 3, 8),
                             (-2, 3, -8),
                             (-2.2, 3, -10.65),
                         ]
                         )
def test_power_func(calc, a, b, expected):
    actual = round(calc.power(a, b), 2)
    assert actual == expected


def test_zero_dev_error(calc):
    with pytest.raises(ZeroDivisionError):
        calc.div(4, 0)


def test_type_error_add(calc):
    with pytest.raises(TypeError):
        calc.add("1")

def test_type_error_power(calc):
    with pytest.raises(TypeError):
        calc.power("1")

def test_type_error_mult(calc):
    with pytest.raises(TypeError):
        calc.mult("1")


def test_type_error_substract(calc):
    with pytest.raises(TypeError):
        calc.substract("1")

def test_type_error_square_root(calc):
    with pytest.raises(TypeError):
        calc.square_root("1")
