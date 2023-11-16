# 1. Створити простий, пустий клас без реалізації - PlaceHolder
class PlaceHolder:
    pass
# 2. Створити клас який приймає при ініціалізації 1 параметр і додати метод
#    який друкує цей параметр

class One_Method_Class:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        return f"Hello, {self.name}"

omc = One_Method_Class("Python")
print(omc.print_name())
