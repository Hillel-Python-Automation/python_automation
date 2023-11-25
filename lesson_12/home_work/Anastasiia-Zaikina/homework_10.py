# Створити простий, пустий клас без реалізації - BaseClass
class BaseClass:
    pass


# Створити клас який успадковується від класу з пункта 1. Додади для ініціалізації ще 1 параметр і ще один метод для виведення нового параметра.
class Dog(BaseClass):
    def __init__(self, breed):
        self.breed = breed

    def print_breed(self):
        print(self.breed)


# Створити клас з методом return_fields() який нічого не повертає (... | pass)

class Animal:
    def return_fields(self):
        pass


# Створити клас, який прийматиме 2 параметри, успадкований від класу з пункту 3 і перевизначити метод return_fields() який виведе поля класу

class Cat(Animal):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def return_fields(self):
        return self.name, self.color


# Створити клас, який прийматиме 3 параметри, успадкований від класу з пункту 3 і перевизначити метод return_fields() який виведе поля класу.

class Rabbit(Animal):
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def return_fields(self):
        return self.name, self.age, self.color
