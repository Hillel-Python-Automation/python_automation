print('''
# Lambda
1. Написати лямбда функцію яка приймає один або 2 аргументи (другому задати значення за замовчуванням рівне 100, 
як у звичайних функціях) та друкує символ переданий як перший аргумент ту кількість раз яка вказана в другому аргументі, 
зробити можливим роботу фнкції не тільки з рядком а й з цифрами.
''')

var_lambda = lambda x, y=100: print(x * y)
var_lambda('t')
var_lambda(2)
print('-' * 30)

print('''
2. Написати лямбда функцію яка приймає 2 числа як аргументи 
та повертає більше з них (використовуйте тернарний if)''')

max_of_two_numbers = lambda x, y: x if x > y else y
print(f'Max of x anf y: {max_of_two_numbers(3, 4)}')
print('-' * 30)

print('''
3. Написати лямбда функція яка нічого не приймає та завжди повертає 10.
''')
lambda_func_10 = lambda: 10
print(lambda_func_10())
print('-' * 30)

print('''
# List comprehension
1. Використовуйте list comprehension, щоб створити новий список, але додайте 6 до кожного елемента.
''')
lst1 = [44, 54, 64, 74, 104]
lst2 = [i + 6 for i in lst1]  # місце для відповіді
print(lst2)
print('-' * 30)

print('''
2. Використовуючи list comprehension, побудуйте список із квадратів кожного елемента в списку.
''')
lst3 = [2, 4, 6, 8, 10, 12, 14]
list4 = [i * i for i in lst3]  # місце для відповіді
print(list4)
print('-' * 30)

print('''
3. Дано словник який складається з транспортних засобів та їх маси в кілограмах. 
Складіть список назв транспортних засобів вагою до 5000 кілограмів. 
У тому самому list comprehension зробіть імена ключів великими регістром.
''')
car_dict = {"Sedan": 1500, "SUV": 2000,
            "Pickup": 2500, "Minivan": 1600,
            "Van": 2400, "Semi": 13600,
            "Bicycle": 7, "Motorcycle": 110}
list5 = [k for k, v in car_dict.items() if v > 5000]  # місце для відповіді
print(list5)
print('-' * 30)

print('''
# Map
Написати функцію яка повертає назву місяця за його номером. 
Використовуючи функцію map() і список який складається з чисел вивести список з навзвами місяців.
''')


def month_name(num):
    match num:
        case 1:
            return 'January'
        case 2:
            return 'February'
        case 3:
            return 'March'
        case 4:
            return 'April'
        case 5:
            return 'May>'
        case 6:
            return 'June'
        case 7:
            return 'July'
        case 8:
            return 'August'
        case 9:
            return 'September'
        case 10:
            return 'October'
        case 11:
            return 'November'
        case 12:
            return 'December'
    return None


nums = list(range(1, 13))
print(list(map(month_name, nums)))
print('-' * 30)
