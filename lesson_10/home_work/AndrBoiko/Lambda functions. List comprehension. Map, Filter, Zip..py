print_func = lambda x, y=100: print(str(x)*y)

print_func('a')
print_func('b', 5)
print_func(5)

max_num = lambda a, b: a if a > b else b

print(max_num(5, 10))

const_ten = lambda: 10

print(const_ten())

list1 = [44, 54, 64, 74, 104]

list2 = [x + 6 for x in list1]

print(list2)

list3 = [2, 4, 6, 8, 10, 12, 14]

list4 = [x**2 for x in list3]

print(list4)

car_dict = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7,
             "Motorcycle": 110}

list5 = [k.upper() for k, v in car_dict.items() if v < 5000]

print(list5)