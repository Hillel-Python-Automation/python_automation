#Арифметична операція:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Помилка: ділення на нуль")

#Робота з колекціями:
my_list = [1, 2, 3]

try:
    element = my_list[5]
except IndexError:
    print("Error")

#try-except-else:
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Помилка: ділення на нуль")
else:
    print("Результат:", result)

#try-except-else-finally:
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Помилка: ділення на нуль")
else:
    print("Результат:", result)
finally:
    print("Block")

#try-except-finally:
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Помилка: ділення на нуль")
finally:
    print("Block")

#try-except з більше ніж трьома except'ами:
my_dict = {"key": "value"}

try:
    value = my_dict["nonexistent_key"]
except KeyError:
    print("Error: key not found")
except TypeError:
    print("Error")
except Exception as e:
    print(f"Another Error: {e}")
