# Reduce
#1.Вивести суму елементів списку з цілих та не цілих чисел

from functools import reduce
from math import isclose

numb = [1, 2, 3, 4, 5, 6, 7, 1.1, 2.5, 3.5]

int_numb = [num for num in numb if isinstance(num, int)]
float_num = [num for num in numb if isinstance(num, float)]# and not isclose(num, int(num))]
sum_func = lambda x, y: x + y

sum_int = reduce(sum_func, int_numb)
print(f'Сума цілих чисел : {sum_int}')

sum_float = reduce(sum_func, float_num)
print(f'Сума не цілих чисел : {sum_float}')

#2.Привести список списків до одновимірного списку використовуючи функцію reduce()
    #було: [ [1,2,3], [3,4,5], [6,7,8], ]
    #має вийти: [1, 2, 3, 3, 4, 5, 6, 7, 8]


list_of_list = [[1,2,3], [3,4,5], [6,7,8]]
sum_list = reduce (lambda x, y: x + y, list_of_list)
print(sum_list)
