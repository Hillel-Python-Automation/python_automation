# Reduce
##1##Вивести суму елементів списку з цілих та не цілих чисел##
print(70*'*')
print('Ex.1')

import functools
import operator

list_1 = [1, 3, 2.5, 6.8, 4, 7, 4.1, 6, 8.9]
print("The sum of all elements is : ", end="")
print(functools.reduce(operator.add, list_1))

##2##Привести список списків до одновимірного списку використовуючи функцію reduce()
#a.було: [ [1,2,3], [3,4,5], [6,7,8], ]
#b.має вийти: [1, 2, 3, 3, 4, 5, 6, 7, 8]
print(70*'*')
print('Ex.2')

list_2 = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
print([i for row in list_2 for i in row])

# Filter
##1##Використовуючи функцію filter() вивести тільки парні числа зі списку.
print(70*'*')
print('Ex.Filter: 1')

list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def my_list_3(x):
    return x % 2 == 0

paried_numbers = list(filter(my_list_3, list_3))
print(f'Paried numbers is:', paried_numbers)

##2##Використовуючи функцію filter() вивести тільки елементи які мають літеру 'а'
print(70*'*')
print('Ex.Filter: 2')

fruits = ['lemon', 'lime', 'banana', 'apricot', 'plum', 'guava', 'melon', 'blueberry', 'watermelon', 'pear']
def my_fruits(x):
    return 'a' in x
a_in_fruits = list(filter(my_fruits, fruits))
print(f'Letter "a" in fruits is present:', a_in_fruits)

##3##ZIP
#1#Зіпнути 2 списки однакової довжини
print(70*'*')
print('Ex.Zip: 1')

name = ('Dyma', 'Olha', 'Ivan', 'Nataly', 'Oleh')
age = ('21', '25', '15', '30', '16')
x = zip(name, age)
print(tuple(x))

#2#Зіпнути 3 списки різної довжини
print(70*'*')
print('Ex.Zip: 2')

first_name = ('James', 'Robert', 'Richard', 'Donald')
last_name =('Jonson', 'Rodrigues', 'Wilson', 'Anderson', 'Martin')
profession =('Astronomer', 'Dentist', 'Farmer', 'Florist', 'Gardener', 'Lawyer')
x = zip(first_name, last_name, profession)
print(tuple(x))

##Recursion## Написати функцію яка виводить ряд Фібоначчі використовуючи рекурсію
print(70*'*')
print('Ex.Recursion: 1')

def fibonacci_list(x, y):
    count = len(y)

    if len(y) < 2:
        return []

    num1 = y[count-2]
    num2 = y[count-1]

    if (num1+num2) < x:
        y = y + [num1+num2]
        return fibonacci_list(x, y)
    else:
        return y

my_fibonacci_list = fibonacci_list(10000, [0, 1])
print('my_fibonacci_list =', my_fibonacci_list)

##Class##
##1##Створити простий, пустий клас без реалізації - PlaceHolder
print(70*'*')
print('Ex.Class: 1')

class PlaceHolder:
    ...
print(PlaceHolder)

##2##Створити клас який приймає при ініціалізації 1 параметр і додати метод який друкує цей параметр
print(70*'*')
print('Ex.Class: 2')

class my_first_class:
    def __init__(self, value):
        self.my_value = value

    def print_value(self):
        print('Value:', self.my_value)

instance_of_my_class = my_first_class('Hello, my name is Dmytro')

instance_of_my_class.print_value()

