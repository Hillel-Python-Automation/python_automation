import csv
import json
import sys

# 1. Створити файл та записати в нього рядок.
file = open("text.txt", 'w')
file.write('Hello, Python!')
file.close()

# 2. Прочитати створений файл та вивести на консоль вміст файлу
try:
    file = open("text.txt", 'r')
    content = file.read()
    print(content)
except FileExistsError as e:
    print(e)
finally:
    file.close()

# 3. Додати ще один рядок до створеного файлу.
try:
    file = open("text.txt", 'w')
    file.write('Hello, Python!\n')
except FileExistsError as e:
    print(e)
finally:
    file.close()

# 4. Прочитати всі рядки з файлу та вивести на консоль.
with open('text.txt') as fl:
    print(fl.read())

# 5. * Записати у файл все що користувач введе з консолі. (Якщо хочете більш ніж один рядок спробуйте використати
# while True і перевірку на введений рядок, типу якщо exit тоді це кінець.)
sys.stdout = open('text5.txt', 'w')
sys.stdout.close()

# 6. Завдання 1-4 прошу зробити міксовано щось через Context manager, а щось класично.
with open('text3.txt', 'w') as fl:
    fl.write("Hello from context manager")

# 7. Використайте прикріплений файл csv та прочитайте його за допомогою модулю csv.
with open('SampleCSVFile_11kb.csv', encoding='cp1252') as sf:
    data = csv.DictReader(sf)

# 8. Використайте прикріплений файл json та прочитайте його за допомогою модулю json.
with open("sample2.json") as sj:
    data2 = json.load(sj)
