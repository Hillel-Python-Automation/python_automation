import pytest

from python_automation.lesson_19.home_work.ValentynVildiaiev.tests.conftest import my_calc


@pytest.mark.parametrize("a, b, expected, description",
[
    (22.1, 3, 25.1, "Adding 22.1 to 3 equals 25.1"),
    (98, -102, -4, "Adding 98 to -102 equals -4"),
    (0, 199, 199, "Adding 0 to 199 equals 199"),
    (99, 91, 190, "Adding 99 to 91 equals 190"),
    (999, 1, 1000, "Adding 999 to 1 equals 1000"),
])
def test_adding_numbers(my_calc, a, b, expected, description):
    res = my_calc.add(a, b)
    assert res == expected, f"Expected {expected},but got {res} for value {a} and {b}. Description: {description}"


@pytest.mark.parametrize("a, b, expected, description",
[
    (22.1, 3, 19.1, "Subtracting 22.1 from 3 equals 19.1"),
    (98, -102, 200, "Subtracting -102 from 98 equals 200"),
    (10, 199, -189, "Subtracting 199 from 10 equals -189"),
    (99, 91, 8, "Subtracting 91 from 99 equals 8"),
    (999, 1, 998, "Subtracting 1 from 999 equals 998"),
])
def test_subtract(my_calc, a, b, expected, description):
    res1 = my_calc.substract(a, b)
    assert res1 == expected, f"Expected {expected},but got {res1} for value {a} and {b}. Description: {description}"


@pytest.mark.parametrize("a, b, expected, description",
[
    (3, 3, 9, "Multiplying 3 by 3 equals 9"),
    (28, 2, 56, "Multiplying 28 by 2 equals 56"),
    (10, 19, 190, "Multiplying 10 by 19 equals 190"),
    (8, 12, 96, "Multiplying 8 by 12 equals 96"),
    (222, 33, 7326, "Multiplying 222 by 33 equals 7326"),
])
def test_multiply(my_calc, a, b, expected, description):
    res2 = my_calc.mult(a, b)
    assert res2 == expected, f"Expected {expected},but got {res2} for value {a} and {b}. Description: {description}"


@pytest.mark.parametrize("a, b, expected, description",
    [
        (9, 3, 3, "Dividing 9 by 3 equals 3"),
        (27, 3, 9, "Dividing 27 by 3 equals 9"),
        (55, 5, 11, "Dividing 55 by 5 equals 11"),
        (98, 4, 24.5, "Dividing 98 by 4 equals 24.5"),
        (200, 5, 40, "Dividing 200 by 5 equals 40"),
    ])
def test_dividing(my_calc, a, b, expected, description):
    res3 = my_calc.div(a, b)
    assert res3 == expected, f"Expected {expected},but got {res3} for value {a} and {b}. Description: {description}"


@pytest.mark.parametrize("a, b, expected, description",
[
    (3, 3, 27, "Raising 3 to the power of 3 equals 27"),
    (27, 3, 19683, "Raising 27 to the power of 3 equals 19683"),
    (5, 5, 3125, "Raising 5 to the power of 5 equals 3125"),
    (8, 4, 4096, "Raising 8 to the power of 4 equals 4096"),
    (20, 5, 3200000, "Raising 20 to the power of 5 equals 3200000"),
])
def test_pow(my_calc, a, b, expected, description):
    res4 = my_calc.power(a, b)
    assert res4 == expected, f"Expected {expected},but got {res4} for value {a} and {b}. Description: {description}"


@pytest.mark.parametrize("a, expected, description",
[
    (5, 2.23606797749979, "Square root of 5 equals 2.23606797749979"),
    (7, 2.6457513110645907, "Square root of 7 equals 2.6457513110645907"),
    (8, 2.8284271247461903, "Square root of 8 equals 2.8284271247461903"),
    (12, 3.4641016151377544, "Square root of 12 equals 3.4641016151377544"),
    (11, 3.3166247903554, "Square root of 11 equals 3.3166247903554"),
])
def test_sqroot(my_calc, a, expected, description):
    res5 = my_calc.square_root(a)
    assert res5 == expected, f"Expected {expected},but got {res5} for value {a}. Description: {description}"
