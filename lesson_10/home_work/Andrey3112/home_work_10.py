#######Lambda
#1)
new_lambda = lambda a, b = 100: str(a) * b

#2)
eshe_lambda = lambda s, d: s if s > d else d

#3)
lambda_10 = lambda: 10
print(lambda_10())

#######List comprehension
#1)
lst1 = [44, 54, 64, 74, 104]
lst2 = [i + 6 for i in lst1]
print(lst2)

#2)
lst3 = [2, 4, 6, 8, 10, 12, 14]
list4 = [i ** 2 for i in lst3]
print(list4)

#3)
car_dict = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7,
         "Motorcycle": 110}
list5 = [i.upper() for i, j in car_dict.items() if j < 5000]
print(list5)

#######Map
def mesyac(chislo):
    months = [
        "jan",
        "feb",
        "mar",
        "apr",
        "may",
        "jun",
        "jul",
        "aug",
        "sep",
        "oct",
        "nov",
        "dec"
    ]
    return months[chislo - 1]
chisla_mesyaca = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
mesyac_name = list(map(mesyac, chisla_mesyaca))
print(mesyac_name)