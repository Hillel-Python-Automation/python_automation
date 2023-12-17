# Створити файл та записати в нього рядок.

with open("file.txt", "w") as file:
    file.write("a file")

# Прочитати створений файл та вивести на консоль вміст файлу

file = open("file.txt", "r")
content = file.read()
print(content)
file.close()

# Додати ще один рядок до створеного файлу.

with open("file.txt", "a") as file:
    file.write("one more row to the file")

# Прочитати всі рядки з файлу та вивести на консоль.

file = open("file.txt", "r")
lines = file.readlines()
for line in lines:
    print(line.strip())
file.close()

# * Записати у файл все що користувач введе з консолі.
# (Якщо хочете більш ніж один рядок спробуйте використати while True і перевірку на введений рядок, типу якщо exit тоді це кінець.)
with open("file.txt", "a") as file:
    while True:
        user_input = input("Please, enter a text or 'exit' to close the program)")
        if user_input.lower() == 'exit':
            break
        file.write(user_input + "\n")

# Використайте прикріплений файл csv та прочитайте його за допомогою модулю csv.

with open('SampleCSVFile.csv', errors='ignore') as sf:
    data = sf.readlines()
    for line in data:
        print(line)

# Використайте прикріплений файл json та прочитайте його за допомогою модулю json.
import json

with open("sample.json", "r") as json_file:
    data = json.load(json_file)
    print(data)