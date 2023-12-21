import json
import csv

#Створити файл та записати в нього рядок.

file = open('created_text.txt', 'x')
try:
    file.write('I have created text to check')
except FileExistsError as exist_error:
    print(exist_error)
finally:
    file.close()

#Прочитати створений файл та вивести на консоль вміст файлу
with open('created_text.txt', 'r') as file:
    content = file.read()
    print(content)


#Додати ще один рядок до створеного файлу.
additional_information = '\nIt is additional text for the file'

with open('created_text.txt', 'a') as file:
    file.write(additional_information)

#Прочитати всі рядки з файлу та вивести на консоль.
try:
    file = open('created_text.txt', 'r')
    file_content = file.read()
except FileNotFoundError as not_found:
    print(not_found)
else:
    print(file_content)
finally:
    file.close()

#Записати у файл все що користувач введе з консолі.
# (Якщо хочете більш ніж один рядок спробуйте використати while True і перевірку на введений рядок, типу якщо exit тоді це кінець.)
while True:
    try:
        file = open('created_text.txt', 'a')
        new_text = input('put your additional text: ')
        if new_text.lower() == 'exit':
            break
    except FileNotFoundError as not_found:
        print(not_found)
    else:
        file.write(f'\n{new_text}')
    finally:
        file.close()

#Використайте прикріплений файл csv та прочитайте його за допомогою модулю csv.
with open('SampleCSVFile_11kb.csv', encoding='cp1252') as csv_file:
    csv_content = csv_file.readlines()
    for line in csv_content:
        print(line)
#Використайте прикріплений файл json та прочитайте його за допомогою модулю json.
with open('sample2.json') as json_file:
    json_content = json.load(json_file)
