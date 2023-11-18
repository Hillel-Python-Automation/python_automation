# Ex.1. Зіпнути 2 списки однакової довжини

list_1 = [1, 2, 3]
list_2 = ['a', 'b', 'c']

zipped_lists = zip(list_1, list_2)
result = list(zipped_lists)
print(result)

# Ex.2.Зіпнути 3 списки різної довжини

list_1_3 = [1, 2, 3]
list_2_3 = ['a', 'b', 'c', 'd']
list_3_3 = [100, 200, 300, 400, 500]

zipped_lists_1 = zip(list_1_3, list_2_3, list_3_3)
result_1 = list(zipped_lists_1)
print(result_1)
