#List compehension Ex_1

lst1 = [44, 54, 64, 74, 104]
lst2 = [x + 6 for x in lst1]
print(lst2)

#List compehension Ex_2
lst3 = [2, 4, 6, 8, 10, 12, 14]

list4 = [x ** 2 for x in lst3]

print(list4)

#List compehension Ex_3
car_dict = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7,
         "Motorcycle": 110}

list5 = [item.upper() for item, weight in car_dict.items() if weight <= 5000]

print(list5)