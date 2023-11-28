# 3. Створити абстрактний клас з абстрактним методом. Створити новий клас
# успадкований від абстрактного класу і створіть об'єкт нового класу.

from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def name(self):
        ...

class Mazda(Car):

    def name(self):
        print("NewModel")


class BMW(Car):

    def name(self):
        print("BMWW")

mazda = Mazda()
mazda.name()

bmw = BMW()
bmw.name()
