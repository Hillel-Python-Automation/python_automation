import csv
import json
import os

task_1 = '1. Створити файл та записати в нього рядок.'
print(task_1)
file = open('task_1', 'w')
file.write(task_1)
file.close()

print('\n')
print('2. Прочитати створений файл та вивести на консоль вміст файлу.')

file_2 = open('task_1', 'r')
print('The file content: ', file_2.read())
file_2.close()

print('\n')
task_3 = '3. Додати ще один рядок до створеного файлу.'
print(task_3)
with open('task_3', 'a') as file_3:
    file_3.write(task_3)

print('\n')
print('4. Прочитати всі рядки з файлу та вивести на консоль.')
with open('task_3', 'r') as file_4:
    print('New file content: ', file_4.read())

print('\n')
print('5. * Записати у файл все що користувач введе з консолі. (Якщо хочете більш ніж один рядок спробуйте використати '
      'while True і перевірку на введений рядок, типу якщо exit тоді це кінець.)')

task_5_file = 'task_5'
if os.path.exists(task_5_file):
    os.remove(task_5_file)

while True:
    user_input = input("Enter your text or command: ")
    if user_input.lower() == 'exit':
        break
    else:
        with open(task_5_file, 'a') as f:
            f.write(user_input + '\n')

with open(task_5_file, 'r') as f:
    print(f"{task_5_file} file content is: ", f.read())

print('\n')
print('7. Використайте прикріплений файл csv та прочитайте його за допомогою модулю csv.')

with open('SampleCSVFile_11kb.csv') as csv_file:
    data = csv.reader(csv_file)
    for line in data:
        print(line)

print('\n')
print('8. Використайте прикріплений файл json та прочитайте його за допомогою модулю json.')

with open('sample2.json', 'r') as json_file:
    json_str = json.load(json_file)
    print(json.dumps(json_str, indent=2))
