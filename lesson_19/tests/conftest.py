import pytest
from lesson_18.app.calc import Calculator


@pytest.fixture()
def calc():
    calc = Calculator()
    print('tests', id(calc))
    return calc


@pytest.fixture()
def calc_link():
    return Calculator


@pytest.fixture()
def calc_call(calc_link):
    return calc_link()


@pytest.fixture()
def subtract_expected_result():
    return 2


@pytest.fixture()
def add_expected_result():
    return 4

