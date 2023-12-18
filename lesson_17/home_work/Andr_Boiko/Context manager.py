# Створити файл та записати в нього рядок.
file = open("file_hw_15", "w")
file.write("File HW_15")
file.close()

# Прочитати створений файл та вивести на консоль вміст файлу
file = open("file_hw_15", "r")
con = file.read()
print("Файл" + con)
file.close()

# Додати ще один рядок до створеного файлу.
file = open("file_hw_15", "a")
file.write("\n""Додати ще один рядок до створеного файлу")
file.close()

# Прочитати всі рядки з файлу та вивести на консоль.
file = open("file_hw_15", "r")
new_con = file.read()
print(new_con)
file.close()

# Використайте прикріплений файл csv та прочитайте його за допомогою модулю csv.
import csv
with open('SampleCSVFile_11kb.csv', encoding='cp1252') as sf:
    data = sf.readlines()
    for line in data:
        print(line)

# Використайте прикріплений файл json та прочитайте його за допомогою модулю json.
import json
print("Використайте прикріплений файл json та прочитайте його за допомогою модулю json.")
with open('sample2.json') as file_json:
    data = file_json.readlines()
    for line in data:
        print(line)