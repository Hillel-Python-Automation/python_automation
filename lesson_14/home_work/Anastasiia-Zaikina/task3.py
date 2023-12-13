"""Створити абстрактний клас з абстрактним методом. Створити новий клас успадкований від абстрактного класу і створіть об'єкт нового класу."""
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def print_animal_sound(self):
        print('Rrrr')
