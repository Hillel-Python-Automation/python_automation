from functools import reduce

print(
    '''
    # Reduce
    1. Вивести суму елементів списку з цілих та не цілих чисел
    ''')
var_list_1 = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]
sum_via_reduce = reduce(lambda x, y: x + y, var_list_1)
print(sum_via_reduce)

print(
    '''
    2. Привести список списків до одновимірного списку використовуючи функцію reduce()
    було: [ [1,2,3], [3,4,5], [6,7,8], ]
    має вийти: [1, 2, 3, 3, 4, 5, 6, 7, 8]
    ''')
var_list_2 = [[1, 2, 3], [3, 4, 5], [6, 7, 8], ]
dd_to_d_via_reduce = reduce(lambda x, y: x + y, var_list_2)
print(dd_to_d_via_reduce)

print(
    '''
    # Filter
    1. Використовуючи функцію filter() вивести тільки парні числа зі списку.
    ''')
var_list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: True if x % 2 == 0 else False, var_list_3)))

print(
    '''
    2. Використовуючи функцію filter() вивести тільки елементи які мають літеру 'а'.
    ''')
words_list = ['Note', 'alpha', "cat", "red", "tend", "ago"]
print(list(filter(lambda x: True if 'a' in str(x) else False, words_list)))

print('''
    # Zip
    1. Зіпнути 2 списки однакової довжини
    ''')
zip_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
zip_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(zip(zip_list_1, zip_list_2)))

print(
    '''
    2. Зіпнути 3 списки різної довжини
    ''')
zip_list_3 = [1, 2, 3, 4, 5]
print(list(zip(zip_list_1, zip_list_3)))

print(
    '''
    # Recursion
    1. Написати функцію яка виводить ряд Фібоначчі використовуючи рекурсію
    ''')


def fibonacci_number(n):
    if n == 0 or n == 1:
        return n
    return fibonacci_number(n - 1) + fibonacci_number(n - 2)


for i in range(10):
    print(fibonacci_number(i))

print(
    '''
    # Class
    1. Створити простий, пустий клас без реалізації - PlaceHolder
    ''')


class PlaceHolder:
    pass


print(PlaceHolder())

print(
    '''
    2. Створити клас який приймає при ініціалізації 1 параметр і додати метод який друкує цей параметр
    ''')


class ClassWithOneParAndMethod:
    def __init__(self, par1):
        self.par1 = par1

    def print_par1(self):
        print(self.par1)


class_2 = ClassWithOneParAndMethod(par1=10)
print(class_2)
class_2.print_par1()
