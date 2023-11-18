# Reduce
from functools import reduce

# Вивести суму елементів списку з цілих та не цілих чисел
lists = [1, 2, 3, 4, 5, 6, 7.8, 6.7]
sum = reduce(lambda a, b: a + b, lists)
print(sum)
# Привести список списків до одновимірного списку використовуючи функцію reduce()
# було: [ [1,2,3], [3,4,5], [6,7,8], ]
# має вийти: [1, 2, 3, 3, 4, 5, 6, 7, 8]
list1 = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
lis = reduce(lambda x, y: x + y, list1)
print(lis)

# Filter
# Використовуючи функцію filter() вивести тільки парні числа зі списку.
li = [1, 2, 3, 4, 5, 6, 7, 8, 6, 7]
print(list(filter(lambda x: x % 2 == 0, li)))
# Використовуючи функцію filter() вивести тільки елементи які мають літеру 'а'.
li2 = ['snow', 'swap', 'apple', 'new', 'over', 'area']
print(list(filter(lambda x: 'a' in x, li2)))

# Zip
# Зіпнути 2 списки однакової довжини
a = ['snow', 'swap', 'apple', 'new', 'over']
b = [1, 2, 3, 4, 5]
d = zip(a, b)
print(list(d))
# Зіпнути 3 списки різної довжини
c = ['car', 3, 'house', 6]
f = zip(a, b, c)
print(list(f))


# Recursion
# Написати функцію яка виводить ряд Фібоначчі використовуючи рекурсію
# Python program to display the Fibonacci sequence
def recursive_fibonachi(n):
    one, two = 0, 1
    for _ in range(n):
        print(one)
        one, two = two, one + two


recursive_fibonachi(12)


# Class
# Створити простий, пустий клас без реалізації - PlaceHolder
class PlaceHolder:
    pass


# Створити клас який приймає при ініціалізації 1 параметр і додати метод який друкує цей параметр
class PrintParam:
    def __init__(self, inside_param):
        self.inside_param = inside_param

    def print_class_param(self):
        print(self.inside_param)


obj = PrintParam('Hello Python!!!')
obj.print_class_param()
