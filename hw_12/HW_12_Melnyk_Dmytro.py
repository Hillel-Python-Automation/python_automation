##Створити клас з абстрактним методом. Створити об'єкт даного класу.##
print(70*'*')
print('Ex. 1')

from abc import ABC, ABCMeta, abstractmethod


class AbsClass(ABC):
    def abs_metod(self):
        pass

class ABSClass_1(AbsClass):
    def abs_method_1(self):
        print('Abstaract method')

a = ABSClass_1()
a.abs_metod()


##Cтворити клас який успадкований від класу ABC або metaclass=ABCMeta і створити його об'єкт.##
print(70*'*')
print('Ex. 2')

class Class_abc(metaclass=ABCMeta):
    def method_abc(self):
        pass

class Class_abc_1(Class_abc):
    print('abc method')

b = Class_abc_1()
b.method_abc()

##Створити абстрактний клас з абстрактним методом.
# Створити новий клас успадкований від абстрактного класу і створіть об'єкт нового класу.##
print(70*'*')
print('Ex. 3')

class Ab_Class(ABC):

    @abstractmethod
    def abs_method(self):
        pass
class Ab_Class_1(Ab_Class):
    def abs_method(self):
        print("Ab_Class")

c = Ab_Class_1()

c.abs_method()

##Створити конструкції try-except для арифметичної операції, роботи з колекціями.##
print(70*'*')
print('Ex. 4')

try:
    dig1 = float(input('Enter digit:'))
    dig2 = float(input('Enter digit:'))
    result = dig1 * dig2
    print('Result:', result)

except Errorvalue:
    print('Error: enter incorrect digit')

try:
    list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    element = int(input("Enter index of element: "))

    value = list_1[element]

    print("Value:", value)

except IndexError:
    print("Error: element is not in the list .")




##Створити конструкції try-except-else.##
print(70*'*')
print('Ex. 5')
try:
    result = 6 / 3
except ZeroDivisionError:
    print('Error: division be zero')
else:
    print(('Result', result))


##Створити конструкції try-except-else-finally.##
print(70*'*')
print('Ex. 6')

try:
    dig1 = float(input('Enter digit:'))
    dig2 = float(input('Enter digit:'))
    result = dig1 / dig2
except ZeroDivisionError:
    print('Error: division be zero')
else:
    print('Result division:', result)
finally:
    print('Good bye')


##Створити конструкції try-except-else-finally.##
print(70*'*')
print('Ex. 7')

try:
    dig1 = float(input('Enter digit:'))
    dig2 = float(input('Enter digit:'))
    result = dig1 / dig2
except ZeroDivisionError:
    print('Error: division be zero')
else:
    print('Result division:', result)
finally:
    print('Good bye')

##Створити конструкції try-except з більше ніж трьома except`ами.##
print(70*'*')
print('Ex. 8')

try:
    dig_3 = input("Enter digits:")
    dig_4 = input("Enter digits:")
    number_1 = float(dig_3)
    number_2 = float(dig_4)
    result = dig_3 / dig_4
except ValueError:
    print("Error:Entered non digits value")

except ZeroDivisionError:
    print("Error: division be zero!")

except TypeError:
    print("Error: Entered unsupported format!")

else:
    print("Result:", result)
