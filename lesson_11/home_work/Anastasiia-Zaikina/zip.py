list_of_elements1 = [1, 2, 3, 4]
list_of_elements2 = [5, 6, 7, 8]
list_of_elements3 = [9, 10]
list_of_elements4 = [11, 12, 13, 14, 15, 16]

# Зіпнути 2 списки однакової довжини
zip_with_same_length = list(zip(list_of_elements1, list_of_elements2))
# Зіпнути 3 списки різної довжини
zip_with_different_length = list(zip(list_of_elements2, list_of_elements3, list_of_elements4))
