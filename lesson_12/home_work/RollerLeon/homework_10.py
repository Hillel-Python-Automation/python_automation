# Створити простий, пустий клас без реалізації - BaseClass
class BaseClass:
    pass
# Створити клас який успадковується від класу з пункта 1. Додади для ініціалізації ще 1 параметр і ще один метод для
# виведення нового параметра.

class DerivedClass(BaseClass):
    def __init__(self, parameter_base, additional_parameter):
        super().__init__()  # Виклик конструктора базового класу (пустого)
        self.parameter = parameter_base
        self.additional_parameter = additional_parameter

    def print_parameters(self):
        print("Base Parameter:", self.parameter)
        print("Additional Parameter:", self.additional_parameter)

derived_obj = DerivedClass("Base Parameter", "Additional Parameter")
derived_obj.print_parameters()


# Створити клас з методом return_fields() який нічого не повертає (... | pass)
class ClassWithMethod:
    def return_fields(self):
        pass

# Створити клас, який прийматиме 2 параметри, успадкований від класу з пункту 3 і перевизначити метод return_fields()
# який виведе поля класу.

class ExtendedClassWithMethod(ClassWithMethod):
    def __init__(self, parameter_base, additional_parameter):
        super().__init__()
        self.parameter = parameter_base
        self.additional_parameter = additional_parameter

    def return_fields(self):
        print(f"Base Parameter: {self.parameter}")
        print(f"Additional Parameter: {self.additional_parameter}")

extended_obj = ExtendedClassWithMethod("Base Parameter", "Additional Parameter")
extended_obj.return_fields()


# Створити клас, який прийматиме 3 параметри, успадкований від класу з пункту 3 і перевизначити метод return_fields()
# який виведе поля класу.

class AnotherExtendedClass(ClassWithMethod):
    def __init__(self, parameter_base, additional_parameter, third_parameter):
        super().__init__()  # Виклик конструктора базового класу без аргументів
        self.parameter = parameter_base
        self.additional_parameter = additional_parameter
        self.third_parameter = third_parameter

    def return_fields(self):
        print(f"Base Parameter: {self.parameter}")
        print(f"Additional Parameter: {self.additional_parameter}")
        print(f"Third Parameter: {self.third_parameter}")

another_extended_obj = AnotherExtendedClass("Base Parameter", "Additional Parameter", "Third Parameter")
another_extended_obj.return_fields()

