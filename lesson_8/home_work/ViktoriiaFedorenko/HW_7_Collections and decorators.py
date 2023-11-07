from collections import namedtuple, Counter, deque, defaultdict
import time

# 1. Counter: Дано рядок у вигляді випадкової послідовності чисел від 0 до 9.
# Потрібно створити словник, який як ключі прийматиме дані числа (тобто ключі будуть типом int),
# а як значення – кількість цих чисел у наявній послідовності.
# Для побудови словника створіть функцію count_it(sequence), що приймає рядок із цифр.
# Функція повинна повернути словник з трьох найчастіше зустрічаються чисел.

numbers = (0, 1, 2, 2, 4, 6, 7, 8, 9, 5, 7, 8, 2, 1, 1, 6, 9, 2)

def count_it(sequence:tuple) -> dict:
    counter = Counter(sequence)
    return dict(counter.most_common(3))


result = count_it(numbers)
print(result)


print()
print("_" * 50)
print()

# 2. namedtuple: Створити namedtuple з іменем Fish та іменними аргументами "name", "species", "tank".
# Створити кілька об'єктів такого namedtuple.
# Вибрати один з них та за допомогою вбудованої функції _asdict() вивести його як словник у консоль.

Fish = namedtuple('Fish', ['name', 'species', 'tank'])
fish = Fish('goldfish', 'comet', 'fish bowl')
fish2 = Fish('goldfish2', 'comet2', 'fish bowl2')
fish3 = Fish('goldfish3', 'comet3', 'fish bowl3')
print(fish._asdict())

print()
print("_" * 50)
print()

# 3. defaultdict: Використовуючи один з варіантів namedtuple створити defaultdict та
# задати йому відповідний тип даних (Згідно тому що маємо в namedtuple) для значень за замовчуванням.

defaulted = defaultdict(lambda: fish2)
defaulted['fish'] = fish
print(defaulted['fish1'])
print(defaulted)


print()
print("_" * 50)
print()

# 4. deque: Створити відповідний пустий список deque, та показати як легко додати на початок,
# на кінець списку не використовуючи індексів, а також як легко видалити з обох кінців.

d = deque()
print(d)
d.append('test')
print(d)
d.appendleft('automation')
print(d)
print("popped element", d.pop())
print(d)
print("popped left element", d.popleft())
print(d)

print()
print("_" * 50)
print()

# 5. Декоратор. Створити декоратор який буде виводити результат функції в консоль,
# функція має щось повертати але не друкувати.

def decorator(func):
    def wrapper():
        print(func())
    return wrapper


@decorator
def phrase():
    return 'La vie est belle'


phrase()
print()
print("_" * 50)
print()

# 6. Завдання з зірочкою. Написати декоратор з аргументами.

def decorator_with_arguments(func):
    def wrapper(arg1, arg2):
        print(f"Print arguments {arg1}, {arg2}")
        func(arg1, arg2)

    return wrapper


@decorator_with_arguments
def print_arguments(value1, value2):
    print(f"Print values {value1}, {value2}")


print_arguments("78", "30")





