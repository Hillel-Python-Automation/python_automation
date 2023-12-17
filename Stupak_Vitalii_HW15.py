#Ex_1.
print('Ex_1.')

filename = 'new_file.txt'
text_to_write = 'Hello John! '

try:
    with open(filename, 'w') as file:
        file.write(text_to_write)
        print(f'Рядок був успішно записаний у файл {filename}.')
except Exception as e:
    print(f'Виникла помилка при записі в файл {e}.')
print(50 * '*')


#Ex_2.
print('Ex_2.')

filename_2 = 'new_file.txt'

with open(filename_2, 'r') as file:
        file_content = file.read()
        if file_content:
            print(f'Вміст файлу {filename_2} : \n {file_content}')
        else:
            print(f'Файл {filename_2} порожній')

print(50 * '*')

#Ex_3.
print('Ex_3.')
filename_3 = 'new_file.txt'
additional_rows = '\n How are you John?'

with open(filename_3, 'a') as file:
    file.write(additional_rows)
    print(f'Рядок був успішно доданий до файлу {filename_3}')

print('Перевірка :')

with open(filename_3, 'r') as file:
        file_content = file.read()

print(f'Вміст файлу {filename_3} : \n {file_content}')

print(50 * '*')

#Ex_4.
print('Ex_4.')
filename_4 = 'new_file.txt'
with open(filename_4, 'r') as file:
    lines = file.readlines()
    print('Зміст файлу :')
    for line in lines:
        print(line.strip())
print(50 * '*')

#Ex_5.
print('Ex_5.')

filename_5 = 'new_file_5.txt'

with open(filename_5, 'w') as file:
        while True:
            user_input = input("Введіть текст (або 'exit' для завершення): ")
            if user_input.lower() == 'exit':
                break
            file.write(user_input + '\n')
print(f'Дані були записані у файл {filename_5}')
print(50 * '*')

#Ex_7.
print('Ex_7.')
import csv

filename_7 = 'SampleCSVFile_11kb.csv'
try:
    with open(filename_7, 'r', newline= '') as file:
        reader = csv.reader(file)
        print('Вміст файлу CSV : ')
        for row in reader:
            print(row)
except FileNotFoundError:
    print(f'Файл {filename_7 } не знайдено.')
except csv.Error as e:
    print(f'Помилка обробки CSV : {e}')
except Exception as e:
    print(f'Виникла помилка : {e}')

print(50 * '*')

#Ex_8.
print('Ex_8.')

import json
filename_8 = 'sample2.json'

try:
    with open(filename_8, 'r') as file:
        data = json.load(file)
        print('Вміст файлу json:')
        print(data)
except FileNotFoundError:
    print(f'Файл {filename_8} не знайдено')
except json.JSONDecodeError as e:
    print(f'Помилка розшифровки  JSON : {e}')
except Exception as e:
    print(f'Виникла помилка : {e}')