# Counter:
# Дано рядок у вигляді випадкової послідовності чисел від 0 до 9.
# Потрібно створити словник, який як ключі прийматиме дані числа (тобто ключі будуть типом int),
# а як значення – кількість цих чисел у наявній послідовності.
# Для побудови словника створіть функцію count_it(sequence), що приймає рядок із цифр.
# Функція повинна повернути словник з трьох найчастіше зустрічаються чисел.

def count_it(sequence):
    counts = {}
    digits = [int(digit) for digit in sequence if digit.isdigit()]

    for digit in digits:
        if digit in counts:
            counts[digit] += 1
        else:
            counts[digit] = 1

    top_three = {}
    for _ in range(3):
        if counts:
            max_digit = max(counts, key=counts.get)
            top_three[max_digit] = counts.pop(max_digit)

    return top_three


sequence = "12345678900987654321"
result = count_it(sequence)
print(result)

# Створити namedtuple з іменем Fish та іменними аргументами "name", "species", "tank".
# Створити кілька об'єктів такого namedtuple.
# Вибрати один з них та за допомогою вбудованої функції _asdict() вивести його як словник у консоль.

from collections import namedtuple

Fish = namedtuple('Fish', 'name species tank')

nemo = Fish(name='Nemo', species='Clownfish', tank='Coral Reef')
dory = Fish(name='Dory', species='Blue Tang', tank='Coral Reef')
gill = Fish(name='Gill', species='Moorish Idol', tank='Coral Reef')

print(nemo._asdict())

#defaultdict:
# Використовуючи один з варіантів namedtuple створити defaultdict
# та задати йому відповідний тип даних
# (Згідно тому що маємо в namedtuple) для значень за замовчуванням.

from collections import defaultdict, namedtuple

Car = namedtuple('Car', ['make', 'model', 'year'])

cars = defaultdict(lambda: Car(make='India',
                              model='Tesla',
                              year=1956))

cars['toyota'] = Car(make='Toyota', model='Camry', year=2022)
cars['ford'] = Car(make='Ford', model='F-150', year=2021)

print(cars['honda'])

#deque:
# Створити відповідний пустий список deque, та показати як легко додати на початок,
# на кінець списку не використовуючи індексів,
# а також як легко видалити з обох кінців.

from collections import deque

deque = deque()
deque.append('a')
deque.append('b')

print(deque)

deque.appendleft('z')
deque.appendleft('y')

print(deque)

deque.pop()
print(deque)

deque.popleft()
print(deque)

#Декоратор.
# Створити декоратор який буде виводити результат функції в консоль,
# функція має щось повертати але не друкувати.

def print_result(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Результат функції:", result)
        return result
    return wrapper