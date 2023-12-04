# Створити клас з абстрактним методом. Створити об'єкт даного класу.
from abc import ABC, abstractmethod, ABCMeta


class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

#obj1 = AbstractClass()

# Створити клас який успадкований від класу ABC або metaclass=ABCMeta і створити його об'єкт.
class NewClass(AbstractClass):
    def abstract_method(self):
        print("NewClass implementing abstract_method")


obj = NewClass()
obj.abstract_method()
print('*' * 40)

# Створити абстрактний клас з абстрактним методом.
# Створити новий клас успадкований від абстрактного класу і створіть об'єкт нового класу.
from abc import ABC, abstractmethod

# Абстрактний клас з абстрактним методом
class AbstractClassWithAbstractMethod(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

# Новий клас, успадкований від абстрактного класу
class NewClass(AbstractClassWithAbstractMethod):
    def abstract_method(self):
        print("Implementation of abstract_method in NewClass")

# Створення об'єкта нового класу
obj3 = NewClass()
obj3.abstract_method()
print('*' * 40)
# Створити конструкції try-except для арифметичної операції, роботи з колекціями.
c = 8
a = 4
b = 4

try:
    result = c / (a - b)
except ZeroDivisionError:
    print("Error: Division by zero")
    print('*' * 40)

# collections
my_list = [1, 4, 2]
try:
    value = my_list[5]  # non-existed element
except IndexError:
    print("Error: Index is not available")
    print('*' * 40)

# Створити конструкції try-except-else
row = 'five'
number5 = 5
try:
    result = row + number5
except TypeError:
    print("Error: can only concatenate str (not 'int') to str")
else:
    print("Result:", result)
print('*' * 40)

# Створити конструкції try-except-else-finally
try:
    result = non_used_variable - 2
except NameError:
    print("Error: a variable is not defined")
else:
    print("Result:", result)
finally:
    print("Thank you for using our program")
print('*' * 40)

# Створити конструкції try-except-finally
try:
    result = a / b
except ZeroDivisionError:
    print("Error: Division by zero")
finally:
    print("You've never wanted to know the result, if b <>0")
print('*' * 40)

# Створити конструкції try-except з більше ніж трьома except`ами
try:
    value = int("abc")
except ValueError:
    print("Error: Invalid conversion to integer")
except TypeError:
    print("Error: Type error")
except Exception as e:
    print(f"Error: {e}")


from abc import ABC, abstractmethod


