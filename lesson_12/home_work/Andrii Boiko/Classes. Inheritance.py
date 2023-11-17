#Створити простий, пустий клас без реалізації - BaseClass

class BaseClass:
    pass

#Створити клас який успадковується від класу з пункта 1. Додади для ініціалізації ще 1 параметр і ще один метод для виведення нового параметра.

class BaseClass:
    pass


class ChildClass(BaseClass):
    def __init__(self, new_param):
        self.new_param = new_param

    def print_new_param(self):
        print(self.new_param)

#Створити клас з методом return_fields() який нічого не повертає (... | pass)

class MyClass:
    def return_fields(self):
        pass

#Створити клас, який прийматиме 2 параметри, успадкований від класу з пункту 3 і перевизначити метод return_fields() який виведе поля класу

class MyClass:
    def return_fields(self):
        pass


class ChildClass(MyClass):
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def return_fields(self):
        print(self.param1, self.param2)


obj = ChildClass("test1", "test2")
obj.return_fields()

#Створити клас, який прийматиме 3 параметри, успадкований від класу з пункту 3 і перевизначити метод return_fields() який виведе поля класу.

class MyClass:
    def return_fields(self):
        pass


class ChildClass(MyClass):
    def __init__(self, param1, param2, param3):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3

    def return_fields(self):
        print(self.param1, self.param2, self.param3)


obj = ChildClass("test1", "test2", "test3")
obj.return_fields()