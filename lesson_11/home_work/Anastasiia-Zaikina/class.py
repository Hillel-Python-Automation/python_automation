# Створити простий, пустий клас без реалізації - PlaceHolder
class Future:
    pass


# Створити клас який приймає при ініціалізації 1 параметр і додати метод який друкує цей параметр
class Dog:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)
