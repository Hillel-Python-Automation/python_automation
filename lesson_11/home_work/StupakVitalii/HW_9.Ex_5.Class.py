# Ex_1. Створити простий, пустий клас без реалізації - PlaceHolder

class PlaceHolder:
    pass

# Ex_2. Створити клас який приймає при ініціалізації 1 параметр
# і додати метод який друкує цей параметр.

class My_Class:
    def __init__(self, parameter):
        self.parameter = parameter
    def print_parameter(self):
        print('Parameter : ', self.parameter)

my_instance = My_Class('Hello my friend !')
my_instance.print_parameter()