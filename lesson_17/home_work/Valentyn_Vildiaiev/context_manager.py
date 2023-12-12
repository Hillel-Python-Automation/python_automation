import csv
import json

# Створити файл та записати в нього рядок.
file = open("VV_HW_15", "w")
file.write("This file is created for homework 15")
file.close()
# Прочитати створений файл та вивести на консоль вміст файлу
file = open("VV_HW_15", "r")
con = file.read()
print("Класичний" + con)
file.close()
# Додати ще один рядок до створеного файлу.
file = open("VV_HW_15", "a")
file.write("\n""This is the second line in the file")
file.close()
# Прочитати всі рядки з файлу та вивести на консоль.
file = open("VV_HW_15", "r")
new_con = file.read()
print(new_con)
file.close()
# * Записати у файл все що користувач введе з консолі.
# (Якщо хочете більш ніж один рядок спробуйте використати while True і перевірку на введений рядок,
# типу якщо exit тоді це кінець.)
file = open("VV_HW_15", "a")
while True:
    user_input = input()
    if user_input.lower() == 'exit':
        break
    file.write("\n" + user_input + "\n")
file.close()
# Використайте прикріплений файл csv та прочитайте його за допомогою модулю csv.
print('*' * 40)
print("Використайте прикріплений файл csv та прочитайте його за допомогою модулю csv.")
with open('SampleCSVFile_11kb.csv') as file_csv:
    data = file_csv.readlines()
    for line in data:
        print(line)

# Використайте прикріплений файл json та прочитайте його за допомогою модулю json.
print('*' * 40)
print("Використайте прикріплений файл json та прочитайте його за допомогою модулю json.")
with open('sample2.json') as file_json:
    data = file_json.readlines()
    for line in data:
        print(line)
