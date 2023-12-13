import os

# Створити конструкції try-except для арифметичної операції, роботи з колекціями.

try:
    print(5 / 0)
except:
    print('You have tried to divide by zero')

new_list = [1, 2]

try:
    print(new_list[2])
except IndexError as error:
    print(error)

# Створити конструкції try-except-else
employees = {
    'name': 'Roman',
    'position': 'manager',
    'salary': 1200
 }
try:
    key = input('Enter a key: ')
    result = employees[key]
except KeyError:
    print(f'We cant find key {key} in employees')
else:
    print(result)

# Створити конструкції try-except-else-finally
employees = {
    'name': 'Roman',
    'position': 'manager',
    'salary': 1200
 }
try:
    key = input('Enter a key: ')
    result = employees[key]
except KeyError:
    print(f'We cant find key {key} in employees')
else:
    print(result)
finally:
    print(employees.keys())

# Створити конструкції try-except-finally
employees = {
    'name': 'Roman',
    'position': 'manager',
    'salary': 1200
 }
try:
    key = input('Enter a key: ')
    result = employees[key]
except KeyError:
    print(f'We cant find key {key} in employees')
finally:
    print(employees.keys())

# Створити конструкції try-except з більше ніж трьома except`ами
path = './test_data'
os.makedirs(path)

try:
    with open(path + '/text_for_test.txt', 'w') as file:
        file.write('Have a greate day!')
except FileExistsError as exist_error:
    print(exist_error)
except FileNotFoundError:
    print(f'Couldn\'t find file with {file} name')
except Exception:
    print('Something get wrong, please verify your code')
finally:
    file.close()
