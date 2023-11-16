# 1. Вивести суму елементів списку з цілих та не цілих чисел
from functools import reduce


def print_sum(a, b):
    return a + b


list1 = [1, 2, 4.5, 11.2]

result = reduce(print_sum, list1)
print(result)

#####
alist = [1, 2, 3.4, 5.5]

result = reduce(lambda a, b: a + b, alist)
print(result)

# 2. Привести список списків до одновимірного списку використовуючи функцію reduce()

a_list = [[1, 2, 3], [3, 4, 5], [6, 7, 8], ]

result = reduce(lambda a, b: a + b, a_list)
print(result)

