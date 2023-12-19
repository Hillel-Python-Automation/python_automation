import math
import sys

import pytest

ddt_add = [
    (2, 2, 4),
    (-2, -2, -4),
    (0, 0, 0),
    (1.1, 1.1, 2.2),
    (1, sys.maxsize, math.pow(2, 63)),

]
DDT_ADD = {
    "argnames": "a, b, expected_result",
    "argvalues": ddt_add,
    "ids": [f"a + b = c | {item[0]} + {item[1]} = {item[2]}" for item in ddt_add]
}


@pytest.mark.parametrize(**DDT_ADD)
def test_add_functionality(init_calc, a, b, expected_result):
    assert init_calc.add(a, b) == expected_result


ddt_substract = [
    (2, 2, 0),
    (-2, -2, 0),
    (0, 0, 0),
    (1.1, 1.1, 0.0),
    (1, -sys.maxsize, math.pow(2, 63)),

]
DDT_SUBSTRACT = {
    "argnames": "a, b, expected_result",
    "argvalues": ddt_substract,
    "ids": [f"a - b = c | {item[0]} - {item[1]} = {item[2]}" for item in ddt_substract]
}


@pytest.mark.parametrize(**DDT_SUBSTRACT)
def test_substract_functionality(init_calc, a, b, expected_result):
    assert init_calc.substract(a, b) == expected_result


ddt_mult = [
    (2, 2, 4),
    (-2, -2, 4),
    (0, 0, 0),
    (1.1, 1.1, 1.21),
    (1, sys.maxsize, 9223372036854775807),

]
DDT_MULT = {
    "argnames": "a, b, expected_result",
    "argvalues": ddt_mult,
    "ids": [f"a * b = c | {item[0]} * {item[1]} = {item[2]}" for item in ddt_mult]
}


@pytest.mark.parametrize(**DDT_MULT)
def test_mult_functionality(init_calc, a, b, expected_result):
    assert init_calc.mult(a, b) == expected_result


ddt_div = [
    (2, 2, 1),
    (-2, -2, 1),
    (0, 0, ZeroDivisionError),
    (1.1, 1.1, 1.0),
    (sys.maxsize, 1, 9223372036854775807.0),

]
DDT_DIV = {
    "argnames": "a, b, expected_result",
    "argvalues": ddt_div,
    "ids": [f"a / b = c | {item[0]} / {item[1]} = {item[2]}" for item in ddt_div]
}


@pytest.mark.parametrize(**DDT_DIV)
def test_div_functionality(init_calc, a, b, expected_result):
    if b == 0:
        with pytest.raises(ZeroDivisionError):
            assert init_calc.div(a, b) == expected_result
    else:
        assert init_calc.div(a, b) == expected_result


ddt_power = [
    (2, 2, 4),
    (-2, 2, 4),
    (0, 0, 1.0),
    (1.1, 1.1, 1.21),
    (sys.maxsize, 1, 9223372036854775807.0),

]
DDT_POWER = {
    "argnames": "a, b, expected_result",
    "argvalues": ddt_power,
    "ids": [f"power({item[0]}, {item[1]}) = {item[2]}" for item in ddt_power]
}


@pytest.mark.parametrize(**DDT_POWER)
def test_power_functionality(init_calc, a, b, expected_result):
    assert init_calc.power(a, b) == expected_result


ddt_square_root = [
    (4, 2),
    (-4, ValueError),
    (0, 0.0),
    (1.21, 1.1),
    (sys.maxsize ** 2, 9223372036854775807.0)
]
DDT_SQUARE_ROOT = {
    "argnames": "a, expected_result",
    "argvalues": ddt_square_root,
    "ids": [f"sqrt({item[0]} = {item[1]}" for item in ddt_square_root]
}


@pytest.mark.parametrize(**DDT_SQUARE_ROOT)
def test_square_root_functionality(init_calc, a, expected_result):
    if a < 0:
        with pytest.raises(ValueError):
            assert init_calc.square_root(a) == expected_result
    else:
        assert init_calc.square_root(a) == expected_result
