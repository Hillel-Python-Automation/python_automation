import abc
from abc import ABC, abstractmethod


# 1. Створити клас з абстрактним методом. Створити об'єкт даного класу.
class AbsTract:
    @abstractmethod
    def abs_method(self):
        pass


class СonСlass(AbsTract):
    def abs_method(self):
        print("Завдання номер 1")


# 2. Створити клас який успадкований від класу ABC або metaclass=ABCMeta і створити його об'єкт.

class Test(ABC):
    @abstractmethod
    def range(self):
        pass


class Year(Test):
    def __init__(self, years):
        self.years = years

    def range(self):
        return self.years


years = Year(1010)
print(years.range())


# 3. Створити клас який успадкований від класу ABC або metaclass=ABCMeta і створити його об'єкт.
class WoodClass(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def abstract_method(self):
        pass


class Tables(WoodClass):
    def abstract_method(self):
        print("Вироби з дерева")
object = Tables()
object.abstract_method()

#4. Створити конструкції try-except для арифметичної операції, роботи з колекціями.

try:
    print(1/0)
except Exception as ex:
    print("Cannot dived by zero")
#5. Створити конструкції try-except-else
a = 5
b = 8
c = 15
x = a+b
y = c+b
try:
    print(a + b)
    if x >20:
        raise Exception("Sorry the numbers are incorrect")
except Exception as e:
    print(e)
else:
    print("Looks good")



#6.Створити конструкції try-except-else-finally
try:
    result = 10/0
except ZeroDivisionError:
    print("Помилка")
else:
    print("result:", result)
finally:
    print("End")
#7. Створити конструкції try-except-finally

try:
    result = 5/0
except ZeroDivisionError:
    print("Невірно")
finally:
    print("Завершено")
#8. Створити конструкції try-except з більше ніж трьома except`ами

try:
    f = int(input("Введіть число: "))
    h= int(input("Введіть друге число: "))
    l = m/q
except ZeroDivisionError:
    print("Друге число не може бути дорівнює нулю.")
except ValueError:
    print("Один із чисел не є цілим числом.")
except TypeError:
    print("Один із чисел не є числом.")
except Exception:
    print("Виникла невідома помилка.")

