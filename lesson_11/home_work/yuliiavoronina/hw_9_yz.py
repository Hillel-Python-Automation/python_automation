from functools import reduce
# Reduce
# 1. Вивести суму елементів списку з цілих та не цілих чисел
int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
float_list = [4.5, 3.25, 0.45, 9.81, 4.46]

sum_int = reduce(lambda a, b: a+b, int_list)
sum_float = reduce(lambda a, b: a+b, float_list)

# 2. Привести список списків до одновимірного списку використовуючи функцію reduce()
# a. було: [ [1,2,3], [3,4,5], [6,7,8], ]
# b. має вийти: [1, 2, 3, 3, 4, 5, 6, 7, 8]
list_list = [[1, 2, 3], [3, 4, 5], [6, 7, 8], ]

reduce_list = reduce(lambda a, b: a + b, list_list)

# Filter
# 3. Використовуючи функцію filter() вивести тільки парні числа зі списку.

even_int = filter(lambda a: True if a % 2 == 0 else False, int_list)

# 4. Використовуючи функцію filter() вивести тільки елементи які мають літеру 'а'.
car_attributes = ['COROLLA', '2015', 'Petrol', 'Automatic']


def contain_a(arr):
    if 'a' in arr:
        return True
    else:
        return False


a_attribute = filter(contain_a, car_attributes)

# Zip
# 5. З`єднати 2 списки однакової довжини

zipped_list_ = list(zip(int_list, int_list))

# 6. З`єднати 3 списки різної довжини
zipped_list_2 = list(zip(int_list, float_list, car_attributes))

# Recursion
# 7. Написати функцію яка виводить ряд Фібоначчі використовуючи рекурсію


def fibonacci_of(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case


fibo_recursion = [fibonacci_of(n) for n in range(15)]

# Class


class PlaceHolder:
    """# 8. Створити простий, пустий клас без реалізації - PlaceHolder"""
    ...


class Easy:
    """# 9. Створити клас який приймає при ініціалізації 1 параметр і додати метод який друкує цей параметр"""
    def __init__(self, parametr):
        self.easy = parametr

    def print_easy(self):
        print(self.easy)


if __name__ == '__main__':
    print("1)", sum_int)
    print("2)", sum_float)
    print("3)", reduce_list)
    print("4)", list(even_int))
    print("5)", (list(a_attribute)))
    print("6)", tuple(zipped_list_))
    print("6)", tuple(zipped_list_2))
    print("7)", fibo_recursion)

    easy = Easy("Hello, it's Easy!")
    easy.print_easy()
