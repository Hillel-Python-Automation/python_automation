"""Створити клас з абстрактним методом. Створити об'єкт даного класу."""

from abc import ABC, abstractmethod


class Animal:

    @abstractmethod
    def print_hello(self):
        print('hello')


if __name__ == '__main__':
    animal = Animal()
