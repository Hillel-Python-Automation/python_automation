# 1. Зіпнути 2 списки однакової довжини

alphabet = ["a", "b", "c", "d"]
nums = [1, 2, 3, 4]

order = list(zip(alphabet, nums))
print(order)

# 2. Зіпнути 3 списки різної довжини

en_alphabet = ["a", "b", "c", "d"]
uk_alphabet = ["а", "б", "в"]
nums = [1, 2, 3, 4, 5]

order = list(zip(en_alphabet, uk_alphabet, nums))
print(order)
