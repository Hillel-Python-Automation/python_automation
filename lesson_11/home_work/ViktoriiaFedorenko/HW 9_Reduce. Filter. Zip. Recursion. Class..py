from functools import reduce


# Reduce

# Вивести суму елементів списку з цілих та не цілих чисел

var_list = [1, 2.5, 3, 4.5, 5, 6.5, 7]

var_sum = reduce(lambda x, y: x+y, var_list)
print(var_sum)


# Привести список списків до одновимірного списку використовуючи функцію reduce()
# було: [ [1,2,3], [3,4,5], [6,7,8], ]
# має вийти: [1, 2, 3, 3, 4, 5, 6, 7, 8]

list_ = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
list_reduce = reduce(lambda x, y: x + y, list_)
print(list_reduce)


# Filter

# Використовуючи функцію filter() вивести тільки парні числа зі списку.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
function_filter = filter(lambda x: True if x % 2 == 0 else False, list1)
print(list(function_filter))

# Використовуючи функцію filter() вивести тільки елементи які мають літеру 'а'.

list2 = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
letter_filter = filter(lambda x: True if 'a' in x.lower() else False, list2)
print(list(letter_filter))


# Zip

# Зіпнути 2 списки однакової довжини

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
zip1 = zip(list1, list2)
print(tuple(zip1))

# Зіпнути 3 списки різної довжини

list3 = ['a', 'b', 'c', 'd']
list4 = ['e', 'f', 'g']
list5 = ['h', 'i', 'j', 'k', 'l', 'm']
zip2 = zip(list3, list4, list5)
print(tuple(zip2))


# Recursion

# Написати функцію яка виводить ряд Фібоначчі використовуючи рекурсію

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number = int(input("Enter number: "))
if number <= 0:
    print("Enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(number):
        print(fibonacci(i))


# Class
#
# Створити простий, пустий клас без реалізації - PlaceHolder

class Class:
    pass


# Створити клас який приймає при ініціалізації 1 параметр і додати метод який друкує цей параметр

class Course:
    def __init__(self, subject):
        self.subject = subject

    def print_subject_details(self):
        print(f"The name of the course is {self.subject}")


course = Course('QA Automation')
course.print_subject_details()


