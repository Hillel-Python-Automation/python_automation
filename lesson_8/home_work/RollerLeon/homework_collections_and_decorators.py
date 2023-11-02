# Counter: Дано рядок у вигляді випадкової послідовності чисел від 0 до 9.
# Потрібно створити словник, який як ключі прийматиме дані числа (тобто ключі будуть типом int),
# а як значення – кількість цих чисел у наявній послідовності.Для побудови словника створіть функцію count_it(sequence),
# що приймає рядок із цифр. Функція повинна повернути словник з трьох найчастіше зустрічаючихся чисел.
from collections import Counter


def row_to_list(the_row):
    # count all the numbers
    counts = Counter(the_row)

    # select 3 most common
    most_frequent = counts.most_common(3)

    # change the result to dic
    dic_sequence = {int(num): count for num, count in most_frequent}

    return dic_sequence


the_row = '124454465445310'
dic_sequence = row_to_list(the_row)
print(dic_sequence)

# namedtuple: Створити namedtuple з іменем Fish та іменними аргументами "name", "species", "tank".
# Створити кілька об'єктів такого namedtuple.
# Вибрати один з них та за допомогою вбудованої функції _asdict() вивести його як словник у консоль.

from collections import namedtuple

Fish = namedtuple('Fish', ['name', 'species', 'tank'])

fish1 = Fish(name='Pirania', species='Really toothy', tank='River')
fish2 = Fish(name='Osetr', species='Delicious', tank='Sea')
fish3 = Fish(name='Moonfish', species='Fictional', tank='The moon')

selected_fish = fish1
fish_dict = selected_fish._asdict()
print(fish_dict)

# defaultdict: Використовуючи один з варіантів namedtuple створити defaultdict та задати йому відповідний тип даних
# (Згідно тому що маємо в namedtuple) для значень за замовчуванням.

from collections import defaultdict, namedtuple

default_fish = Fish(name='default', species='default', tank='default')

fish_dict = defaultdict(lambda: default_fish)

print(fish_dict['some_fish'])

# deque: Створити відповідний пустий список deque, та показати як легко додати на початок,
# на кінець списку не використовуючи індексів, а також як легко видалити з обох кінців.

from collections import deque

my_deque = deque()

# add
my_deque.append('right')
my_deque.appendleft('left')

print(my_deque)  # should be ([left, right])

# remove
right_element = my_deque.pop()
left_element = my_deque.popleft()

# removed values
print(left_element)
print(right_element)

print(my_deque)


# Декоратор. Створити декоратор який буде виводити результат функції в консоль,
# функція має щось повертати але не друкувати.
def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Result", result)
        return result

    return wrapper


@decorator
def add(a, b):
    return a + b


result = add(1, 2)
