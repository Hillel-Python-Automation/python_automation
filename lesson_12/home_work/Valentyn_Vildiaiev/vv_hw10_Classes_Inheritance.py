# 1.Створити простий, пустий клас без реалізації - BaseClass
class SimpleOne:
    pass


# 2.Створити клас який успадковується від класу з пункта 1.
# Додади для ініціалізації ще 1 параметр і ще один метод для виведення нового параметра.
class SecondOne(SimpleOne):
    def __init__(self, params):
        self.params = params

    def print_param(self):
        print(self.params)


# 3.Створити клас з методом return_fields() який нічого не повертає (... | pass)
class ReturnOne:
    def return_fields(self):
        pass


# 4.Створити клас, який прийматиме 2 параметри, успадкований від класу з пункту 3 і
# перевизначити метод return_fields() який виведе поля класу.
class RevisedOne(ReturnOne):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def return_fields(self):
        print(self.p1, self.p2)


# 5.Створити клас, який прийматиме 3 параметри, успадкований від класу з пункту 3 і
# перевизначити метод return_fields() який виведе поля класу.
class RevisedAgain(ReturnOne):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def return_fields(self):
        print(self.p1, self.p2, self.p3)
