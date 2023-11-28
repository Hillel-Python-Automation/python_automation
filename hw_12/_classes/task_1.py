# 1. Створити клас з абстрактним методом. Створити об'єкт даного класу.

from abc import ABC, abstractmethod


class AbstractClass(ABC):

    @abstractmethod
    def method(self):
        pass


ac = AbstractClass()
