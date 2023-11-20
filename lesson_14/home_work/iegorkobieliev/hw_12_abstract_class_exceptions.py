from abc import ABC, abstractmethod
import random

print('''1. Створити клас з абстрактним методом. Створити об'єкт даного класу.''')


class ClassWithAbstractMethod:
    @abstractmethod
    def abstract_method(self):
        pass


cwam = ClassWithAbstractMethod()
print(cwam)
print('_' * 30)

print('''2. Створити клас який успадкований від класу ABC або metaclass=ABCMeta і створити його об'єкт.''')


class FromABC(ABC):
    pass


from_abc = FromABC()
print(from_abc)
print('_' * 30)

print('''3. Створити абстрактний клас з абстрактним методом. Створити новий клас успадкований від абстрактного класу 
і створіть об'єкт нового класу.''')


class AbstractClassWithAbstractMethod(ABC):
    def abstract_method(self):
        pass


class ClassTask3(AbstractClassWithAbstractMethod):
    def abstract_method(self):
        return 'ClassTask3'


ct3 = ClassTask3()
print(ct3)
print(ct3.abstract_method())
print('_' * 30)

print('''4. Створити конструкції try-except для арифметичної операції, роботи з колекціями.''')

try:
    result = 100 / 0
except ZeroDivisionError:
    print('You cannot divide by 0.')

my_list = [1, 2]
try:
    desired_value = my_list[2]
except IndexError:
    print('Index is out of the range.')
print('_' * 30)

print('''5. Створити конструкції try-except-else''')
try:
    value = random.choice([1, 0])
    result = 1 / value
except ZeroDivisionError as zde:
    print(f'Zero division error is generated: {zde}.')
else:
    print('Zero division error is NOT generated.')
print('_' * 30)

print('''6. Створити конструкції try-except-else-finally''')
try:
    value = random.choice([1, 0])
    result = 1 / value
except ZeroDivisionError as zde:
    print(f"except branch. ZDE: {zde}.")
else:
    print("else branch.")
finally:
    print('It will be printed anyway.')
print('_' * 30)

print('''7. Створити конструкції try-except-finally''')
try:
    value = random.choice([1, 0])
    result = 1 / value
except ZeroDivisionError as zde:
    print(f"except branch. ZDE: {zde}.")
finally:
    print('It will be printed anyway.')
print('_' * 30)

print('''8. Створити конструкції try-except з більше ніж трьома except`ами''')
for i in [0, 1, 2]:
    try:
        match i:
            case 0:
                raise ZeroDivisionError(f'i = {i}')
            case 1:
                raise ValueError(f'i = {i}')
            case 2:
                raise IndexError(f'i = {i}')
    except ZeroDivisionError as zde:
        print(f"ZDE: {zde}")
    except ValueError as ve:
        print(f"VE: {ve}")
    except IndexError as ie:
        print(f"IE: {ie}")
    print('_' * 30)
