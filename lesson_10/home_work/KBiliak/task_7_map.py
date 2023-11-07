# Написати функцію яка повертає назву місяця за його номером. Використовуючи
# функцію map() і список який складається з чисел вивести список з навзвами
# місяців.

mon = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

def map_month(i):
    return mon[i-1]


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

pp = list(map(map_month, num))
print(pp)


