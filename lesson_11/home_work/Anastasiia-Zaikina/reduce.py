from functools import reduce

# Вивести суму елементів списку з цілих та не цілих чисел
list_of_elements = [1, 2, 3, 4, 5.5, 6, 7]
sum_of_elements = reduce(lambda first_element, second_element: first_element + second_element, list_of_elements)
print(sum_of_elements)

# Привести список списків до одновимірного списку використовуючи функцію reduce()
list_of_lists = [[1, 2, 3], [3, 4, 5], [6, 7, 8], ]
common_list = reduce(lambda first_list, second_list: first_list + second_list, list_of_lists)
