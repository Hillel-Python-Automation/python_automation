# Lambda

# 1. Написати лямбда функцію яка приймає один або 2 аргументи
# (другому задати значення за замовчуванням рівне 100, як у звичайних функціях)
# та друкує символ переданий як перший аргумент ту кількість раз яка вказана
# в другому аргументі, зробити можливим роботу функції не тільки з рядком а й з цифрами.

lambda_two_arguments = lambda arg1, arg2=100: str(arg1) * arg2
print(lambda_two_arguments(4))

# 2. Написати лямбда функцію яка приймає 2 числа як аргументи та повертає більше з них (використовуйте тернарний if)

var_max = lambda x, y: x if x > y else y
print(var_max(1, 4))

# 3. Написати лямбда функція яка нічого не приймає та завжди повертає 10.

var_empty = lambda: 10
print(var_empty())

# List comprehension

# Використовуйте list comprehension, щоб створити новий список, але додайте 6 до кожного елемента.

lst1 = [44, 54, 64, 74, 104]
lst2 = [item + 6 for item in lst1]
print(lst2)

# Використовуючи list comprehension, побудуйте список із квадратів кожного елемента в списку.

lst3 = [2, 4, 6, 8, 10, 12, 14]
list4 = [item ** 2 for item in lst3]
print(list4)

# Дано словник який складається з транспортних засобів та їх маси в кілограмах.
# Складіть список назв транспортних засобів вагою до 5000 кілограмів. У тому самому list comprehension зробіть імена ключів великими регістром.

car_dict = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7,
            "Motorcycle": 110}
list5 = [(k.upper(), v) for k, v in car_dict.items() if v < 5000]
print(list5)

# Map

# Написати функцію яка повертає назву місяця за його номером.
# Використовуючи функцію map() і список який складається з чисел вивести список з назвами місяців.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12]


def month(month_number: int) -> str:
    if month_number in [1]:
        return 'January'
    elif month_number in [2]:
        return 'February'
    elif month_number in [3]:
        return 'March'
    elif month_number in [4]:
        return 'April'
    elif month_number in [5]:
        return 'May'
    elif month_number in [6]:
        return 'June'
    elif month_number in [7]:
        return 'July'
    elif month_number in [8]:
        return 'August'
    elif month_number in [9]:
        return 'September'
    elif month_number in [10]:
        return 'October'
    elif month_number in [11]:
        return 'November'
    elif month_number in [12]:
        return 'December'
    else:
        return 'Undefined month'


month_name = list(map(month, numbers))
print(month_name)
