# Написати лямбда функцію яка приймає один або 2 аргументи
# (другому задати значення за замовчуванням рівне 100, як у звичайних функціях)
# та друкує символ переданий як перший аргумент ту кількість раз яка вказана в другому аргументі,
# зробити можливим роботу фнкції не тільки з рядком а й з цифрами.

var_lmbda = lambda a, b=100: print(str(a)*int(b))


var_lmbda('x', 9)

# Написати лямбда функцію яка приймає 2 числа як аргументи
# та повертає більше з них (використовуйте тернарний if)
var_lmbda2 = lambda a, b: print(a if a > b else b)


var_lmbda2(11, 9)

# Написати лямбда функція яка нічого не приймає та завжди повертає 10.
var_lmbda3 = lambda: print(10)

var_lmbda3()

# List comprehension

#Використовуйте list comprehension, щоб створити новий список, але додайте 6 до кожного елемента.
lst1 = [44, 54, 64, 74, 104]

lst2 = [x + 6 for x in lst1] # місце для відповіді
print(lst2)

#Використовуючи list comprehension, побудуйте список із квадратів кожного елемента в списку.
lst3 = [2, 4, 6, 8, 10, 12, 14]

list4 = [x ** 2 for x in lst3] # місце для відповіді
print(list4)
#Дано словник який складається з транспортних засобів та їх маси в кілограмах.
#Складіть список назв транспортних засобів вагою до 5000 кілограмів.
#У тому самому list comprehension зробіть імена ключів великими регістром.
car_dict = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7,
         "Motorcycle": 110}
list5 = [key.upper() for key, value in car_dict.items() if value <=5000] # місце для відповіді
print(list5)

# Map

#Написати функцію яка повертає назву місяця за його номером.
#Використовуючи функцію map() і список який складається з чисел вивести список з навзвами місяців.
def get_month(month_number):
    month_name = [
        "January","February","March",
        "April","May","June","July",
        "August","September","October",
        "November","December"
    ]
    if 1 <= month_number <=12:
        return month_name[month_number -1]
    else:
        print("We don't have such month number")

number_of_month = [2,5,7,1,5]
month_names = list(map(get_month,number_of_month))
print(month_names)
