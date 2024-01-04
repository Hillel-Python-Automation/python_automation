import pytest
from python_automation.Lesson_18.app.calc import Calculator

@pytest.fixture(scope='function')
def my_fixture():
    return Calculator()

@pytest.fixture(scope='session')
def my_fixture():
    yield
