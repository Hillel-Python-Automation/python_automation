import pytest


@pytest.mark.parametrize(
    'first_value, second_value, expected_result',
    [
        (6, 2, 3),
        (4, 0, ZeroDivisionError),
        (2, 2, 1),
        (-4, 2, -2)
    ]
)
def test_divide(calculator, first_value, second_value, expected_result):
    if second_value == 0:
        with pytest.raises(expected_result):
            calculator.div(first_value, second_value)
    else:
        calculator.div(first_value, second_value) == expected_result


@pytest.mark.parametrize(
    'first_value, second_value, expected_result',
    [
        (3, 3, 9),
        (5, 0, 0),
        (6, 1, 6),
        (-2, -3, 6)
    ]
)
def test_mult(calculator, first_value, second_value, expected_result):
    calculator.mult(first_value, second_value) == expected_result


@pytest.mark.parametrize(
    'first_value, second_value, expected_result',
    [
        (2, 6, 64),
        (4, 0, 1),
        (0, 8, 0),
        (2, -2, 0.25)
    ]
)
def test_power(calculator, first_value, second_value, expected_result):
    calculator.power(first_value, second_value) == expected_result


@pytest.mark.parametrize(
    'first_value, second_value, expected_result',
    [
        (2, 2, 0),
        (-3, -3, 0),
        (-2, 4, -6),
        (6, -2, 8)
    ]
)
def test_subtract(calculator, first_value, second_value, expected_result):
    calculator.substract(first_value, second_value) == expected_result


@pytest.mark.parametrize(
    'value, expected_result',
    [
        (25, 5),
        (1, 1),
        (0, 0),
        (-5, ValueError)
    ]
)
def test_square_root(calculator, value, expected_result):
    if value < 0:
        with pytest.raises(expected_result):
            calculator.square_root(value)
    else:
        calculator.square_root(value) == expected_result
