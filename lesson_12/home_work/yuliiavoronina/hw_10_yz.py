
class BaseClass:
    """# 1. Створити простий, пустий клас без реалізації - BaseClass"""
    ...


class SecondClass(BaseClass):
    """# 2. Створити клас який успадковується від класу з пункта 1. Додади для ініціалізації ще 1 параметр
    # і ще один метод для виведення нового параметра."""
    def __init__(self, parametr):
        self.easy = parametr

    def print_easy(self):
        print(self.easy)


class ThirdClass:
    """# 3. Створити клас з методом return_fields() який нічого не повертає (... | pass)"""
    def return_fields(self):
        pass


class FourthClass(ThirdClass):
    """# 4. Створити клас, який прийматиме 2 параметри, успадкований від класу з пункту 3 і перевизначити метод
    # return_fields() який виведе поля класу."""
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def return_fields(self):
        print(self.a, self.b)


class FifthClass(ThirdClass):
    """# 5. Створити клас, який прийматиме 3 параметри, успадкований від класу з пункту 3 і перевизначити метод
    # return_fields() який виведе поля класу."""
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def return_fields(self):
        print(self.a, self.b, self.c)
