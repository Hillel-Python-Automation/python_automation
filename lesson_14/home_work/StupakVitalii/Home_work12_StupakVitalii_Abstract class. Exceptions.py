#Ex_1.
print(50 * '*')
print('Ex_1.')
from abc import ABC, abstractmethod
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

try:
    instance = AbstractClass()
except TypeError as e:
    print(f'TypeError: {e}')

#Ex_2.
print(50 * '*')
print('Ex_2.')
class NewClass(AbstractClass):
    def abstract_method(self):
        print('Implementation of abstract_method in NewClass')

object_1 = NewClass()
object_1.abstract_method()

#Ex_3.
print(50 * '*')
print('Ex_3.')
class NewClass1(AbstractClass):
    def abstract_method(self):
        print('Implementation of abstract_method in NewClass1')

object_2 = NewClass1()
object_2.abstract_method()

#Ex_4.
print(50 * '*')
print('Ex_4.')
try:
    res = 50 + 1
    print(res)
except Exception as ex:
    print('Division by zero')

#Ex_5.
print(50 * '*')
print('Ex_5.')
try:
    result = 10 * 10
except ZeroDivisionError as e:
    print(f'Result : {e}')
else:
    print(f'Result : {result}')

#Ex_6.
print(50 * '*')
print('Ex_6.')

try:
    result_1 = 10 + 90
except ZeroDivisionError as e:
    print(f'Result : {e}')
else:
    print(f'Result : {result_1}')
finally:
    print('Finally block executed regardless of exception')

#Ex_7.
print(50 * '*')
print('Ex_7.')
try:
    result_2 = 10 / 0
except ZeroDivisionError as e:
    print(f'Result : {e}')
finally:
    print('Not executed. Division by zero')

#Ex_8.
print(50 * '*')
print('Ex_8.')

try:
    val_1 = float(input('Enter value 1 :'))
    val_2 = float(input('Enter value 2 :'))
    print(val_1 / val_2)
except ZeroDivisionError as zde:
    print(f' Result : {zde}')
except ValueError as ve:
    print('Please fix entering value '.format(ve))
except ArithmeticError as ae:
    print('Arithmetic error, please fix ')
except Exception as ex:
    print('Fix youe errorrs')