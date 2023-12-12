# 1. Створити файл та записати в нього рядок.

with open("text.txt", "a") as file:
    file.write("Hello" + "\n")

# file_to_write = open("text.txt", "a")
# try:
#     print(file_to_write.write("Hi there" + "\n"))
# finally:
#     file_to_write.close()


# 2. Прочитати створений файл та вивести на консоль вміст файлу.

with open("text.txt", "r") as file:
    print(file.read())

# 3. Додати ще один рядок до створеного файлу.

with open("text.txt", "a") as file:
    file.write("hello to you\n")

# 4.Прочитати всі рядки з файлу та вивести на консоль.

file_to_read = open("text.txt", "r")
try:
    print(file_to_read.read())
finally:
    file_to_read.close()

# 5. * Записати у файл все що користувач введе з консолі. (Якщо хочете більш ніж
# один рядок спробуйте використати while True і перевірку на введений рядок,
# типу якщо exit тоді це кінець.)

with open("text.txt", "a") as file:
    while True:
        user_input = input("Enter your row: ")
        if user_input == "exit":
            break
        file.write(user_input +"\n")

with open("text.txt", "r") as file:
    print(file.read())


