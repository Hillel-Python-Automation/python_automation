# Reduce

   # Вивести суму елементів списку з цілих та не цілих чисел

first_list = [1, 4.8, 8, 4.35, 6]
total_sum = sum(first_list)
print("Сума:", total_sum)

   # Привести список списків до одновимірного списку використовуючи функцію reduce()
   # було: [ [1,2,3], [3,4,5], [6,7,8], ]
   # має вийти: [1, 2, 3, 3, 4, 5, 6, 7, 8]
from functools import reduce
list_of_lists = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
simple_list = reduce(lambda x, y: x + y, list_of_lists)
print(simple_list)

# Filter

  #  Використовуючи функцію filter() вивести тільки парні числа зі списку.
numbers = [5, 7, 9, 4, 5, 6, 9, 2, 1]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Парні числа:", even_numbers)

  # Використовуючи функцію filter() вивести тільки елементи які мають літеру 'а'.
contains_a = ['sjhr', 'sdkrma', 'as3', 'aaa', ' a ', '1a1', '1']
only_a = list(filter(lambda x: 'a' in x, contains_a))
print("Тільки елементи які мають літеру 'а':", only_a)
# Zip

  # Зіпнути 2 списки однакової довжини
list1 = [1, 6, 3.5, 8]
list2 = ['a', 'b', 'c', 'd']
zipped_list = list(zip(list1, list2))
print("Зіпнутий список з 2-х:", zipped_list)

  # Зіпнути 3 списки різної довжини
from itertools import zip_longest

list_1 = [1, 3, 8, 9]
list_2 = ['a', 'b', 'c']
list_3 = ['x1', 'y2', 'z3', 'w4', 'q5']

zipped_from3 = list(zip_longest(list_1, list_2, list_3, fillvalue=None))

print("Зіпнутий список p 3-х:", zipped_from3)


# Recursion

  # Написати функцію яка виводить ряд Фібоначчі використовуючи рекурсію
def fibonacci(n, a=0, b=1):
    if n == 0:
        return []
    elif n == 1:
        return [a]
    else:
        return [a] + fibonacci(n-1, b, a+b)

# n = count of the numbers
n = 10
result = fibonacci(n)
print(result)

# Class

  # Створити простий, пустий клас без реалізації - PlaceHolder
class PlaceHolder:
    pass
  # Створити клас який приймає при ініціалізації 1 параметр і додати метод який друкує цей параметр
class MyClass:
    def __init__(self, parameter):
        self.parameter = parameter

    def print_parameter(self):
        print(self.parameter)

obj = MyClass("Hello, World!")
obj.print_parameter()
