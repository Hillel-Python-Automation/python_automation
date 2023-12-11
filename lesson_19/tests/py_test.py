import sys

import pytest


@pytest.fixture
def add_expected_result():
    return 4


@pytest.mark.smoke
@pytest.mark.add_function
def test_add_two_numbers(calc, add_expected_result):
    print(id(calc))
    assert calc.add(2, 2) == add_expected_result


@pytest.mark.smoke
@pytest.mark.add_function
def test_add_two_negative_numbers(calc):
    print(id(calc))
    assert calc.add(-2, -20) == -22


@pytest.mark.smoke
@pytest.mark.subtract_function
def test_subtract_func(calc, subtract_expected_result):
    print(id(calc))
    assert calc.substract(4, 2) == subtract_expected_result


@pytest.mark.smoke
@pytest.mark.subtract_function
@pytest.mark.skip(reason='Just because')
def test_subtract_function(calc):
    print(id(calc))
    assert calc.substract(4, -2) == 6


@pytest.mark.smoke
def test_error_handling(calc):
    with pytest.raises(ZeroDivisionError):
        calc.div(3, 0)


@pytest.mark.smoke
@pytest.mark.parametrize(
    # 'a,b,expected',
    ('a', 'b', 'expected'),
    [
        (+2, +3, +5),
        (2, -2, 0),
        (-2, -2, -4),
        pytest.param(11, 10, 21, marks=pytest.mark.skipif(sys.platform == 'linux', reason='The tests shouldn\'t be executed on linux')),
        pytest.param(10, 10, 20, marks=pytest.mark.skip(reason='Just Because')),
        (5, 5, 10),
        pytest.param('a', 5, 'error', marks=pytest.mark.xfail(run=False)),
        pytest.param('a', 5, 'error', marks=pytest.mark.xfail(reason="JIRA Ticket")),
    ]
)
def test_add_function(calc, a, b, expected):
    assert calc.add(a, b) == expected


