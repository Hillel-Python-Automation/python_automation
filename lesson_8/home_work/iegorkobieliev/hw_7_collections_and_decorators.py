import random
from collections import Counter, namedtuple, defaultdict, deque

print('''
1. Counter: Дано рядок у вигляді випадкової послідовності чисел від 0 до 9.
Потрібно створити словник, який як ключі прийматиме дані числа (тобто ключі будуть типом int),
а як значення – кількість цих чисел у наявній послідовності.
Для побудови словника створіть функцію count_it(sequence),
що приймає рядок із цифр. Функція повинна повернути словник з трьох найчастіше зустрічаються чисел.
''')

random_list_of_int = random.choices(range(0, 10), k=10)
random_str = ''.join(str(i) for i in random_list_of_int)
print('random_str:')
print(random_str)


def count_it(sequence):
    return dict(Counter(sequence).most_common(3))


print(f'Three most common characters: {count_it(random_str)}')

print('''\n
2. namedtuple: Створити namedtuple з іменем Fish та іменними аргументами "name", "species", "tank". 
Створити кілька об'єктів такого namedtuple. Вибрати один з них та за допомогою вбудованої функції _asdict() 
вивести його як словник у консоль.
''')
Fish = namedtuple('Point', ['name', 'species', 'tank'])
fish_1 = Fish(name='Fish_1', species='Species_1', tank="Tank_1")
fish_2 = Fish(name='Fish_2', species='Species_2', tank="Tank_2")
print(f'Fish_2 = {fish_2._asdict()}')

print('''\n
3. defaultdict: Використовуючи один з варіантів namedtuple створити defaultdict та задати йому відповідний тип даних 
(Згідно тому що маємо в namedtuple) для значень за замовчуванням.
''')

def_dict = defaultdict(str)
print(f'Default dictionary: {def_dict}')
def_dict['first'] = 1
def_dict['third'] = 3
print(def_dict['first'])
print(def_dict['second'])
print(def_dict['third'])

print('''
4. deque: Створити відповідний пустий список deque, та показати як легко додати на початок, 
на кінець списку не використовуючи індексів, а також як легко видалити з обох кінців.
''')

deque_list = deque()
deque_list.appendleft(1)
deque_list.appendleft('left')
deque_list.append(2)
deque_list.append('right')
print(deque_list)
deque_list.popleft()
print(deque_list)
deque_list.pop()
print(deque_list)

print('''
5. Декоратор. Створити декоратор який буде виводити результат функції в консоль, 
функція має щось повертати але не друкувати.
''')


def decorator_func(some_func):
    def func_wrapper():
        print('Before func_wrapper')
        print(f'Print the result of execution some_func: {some_func()}')
        print("After func_wrapper")

    return func_wrapper


@decorator_func
def func_return_true():
    return True


func_return_true()

print('''
6. Завдання з зірочкою. Написати декоратор з аргументами. 
Приклад не був показаний на занятті але є в матеріалах до заняття номер 9.  
''')


def decorator_with_args(func):
    def wrapper_args_level(arg1, arg2):
        print('1. Before func.')
        print(f'2. Result of func execution: {func(arg1, arg2)}.')
        print("3. After func.")
    return wrapper_args_level


@decorator_with_args
def sum_of_two_numbers(x, y):
    return x + y


sum_of_two_numbers(10, 20)
