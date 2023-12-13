"""Створити клас який успадкований від класу ABC або metaclass=ABCMeta і створити його об'єкт."""
from abc import ABC


class People(ABC):
    pass


if __name__ == '__main__':
    person = People()
