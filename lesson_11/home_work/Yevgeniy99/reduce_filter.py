# Reduce
# 1.Вивести суму елементів списку з цілих та не цілих чисел
import functools
import operator
import itertools
from functools import reduce

list_one = {1, 3, 5, 2.3, 3.7, 5, 9}
v_reduce = reduce(lambda a, b: a + b, list_one)
print(v_reduce)
# Привести список списків до одновимірного списку використовуючи функцію reduce()
# було: [ [1,2,3], [3,4,5], [6,7,8], ]
# має вийти: [1, 2, 3, 3, 4, 5, 6, 7, 8]

m_list = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
result = reduce(lambda x, y: x + y, m_list)
print(result)

# Filter

# 1. Використовуючи функцію filter() вивести тільки парні числа зі списку.
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = list(filter(lambda x: x % 2 == 0, list_numbers))
print(results)
# 2. Використовуючи функцію filter() вивести тільки елементи які мають літеру 'а'.

list_words = ['Anaconda', 'Ball', 'Flex', 'Scooter', 'Harry', 'Ron', 'Music']
results = list(filter(lambda x: 'a' in x, list_words))
print(results)

# Zip

# 3. Зіпнути 2 списки однакової довжини
f_names = ("Harry", "Jhon", "Aragorn")
l_names = ("Potter", "Whick", "Elessar")
fl_names = zip(f_names, l_names)
print(tuple(fl_names))
# 4. Зіпнути 3 списки різної довжини
a = ("Tom", "Cat", "Logan")
b = ("Tyrel", "Bladerunner", "Cyberpunk", "Forza")
c = ("Ratchet", "Clank", "Peter", "Alice", "Digimon", "Mario", "Sin")
y = zip(a, b, c)
print(tuple(y))
# Написати функцію яка виводить ряд Фібоначчі використовуючи рекурсію

import math


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))


for i in range(10):
    print(fibonacci(i))


# Class
# 1. Створити простий, пустий клас без реалізації - PlaceHolder
class PlaceHolder:
    pass


# 2. Створити клас який приймає при ініціалізації 1 параметр і додати метод який друкує цей параметр
class Names:
    def __init__(self, name):
        self.name = name
    def print_name(self):
        print(f"My Name is:{self.name}")
test_obj = Names("Jhon")
test_obj.print_name()


