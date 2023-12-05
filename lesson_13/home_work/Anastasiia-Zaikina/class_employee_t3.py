"""Створити клас з 2 змінними (_a and __a), Створити об'єкт класу та показати доступ до цих змінних.
(Очікувано отримаємо помилку при доступі до __а)"""


class Employee:
    def __init__(self, name, age):
        self._name = name
        self.__age = age


if __name__ == '__main__':
    oleh = Employee('Oleh', 28)
    print(oleh._name)
    print(oleh.__age)
