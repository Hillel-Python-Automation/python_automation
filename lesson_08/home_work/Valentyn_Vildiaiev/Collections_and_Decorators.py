from collections import namedtuple,defaultdict,deque
#Counter: 
# Дано рядок у вигляді випадкової послідовності чисел від 0 до 9. 
# Потрібно створити словник, який як ключі прийматиме дані числа (тобто ключі будуть типом int), 
# а як значення – кількість цих чисел у наявній послідовності. 
# Для побудови словника створіть функцію count_it(sequence), що приймає рядок із цифр. 
# Функція повинна повернути словник з трьох найчастіше зустрічаються чисел.

def count_it(sequence):
    new_dict = {}
    for char in inp_str:
        if char.isdigit():
            digit = int(char)  
        if digit in new_dict:
            new_dict[digit]+= 1
        else:
            new_dict[digit] = 1
    return new_dict

inp_str = '90123465789'
res = count_it(inp_str)
print(res)   
            

#namedtuple: 
# Створити namedtuple з іменем Fish та іменними аргументами "name", "species", "tank". 
# Створити кілька об'єктів такого namedtuple. 
# Вибрати один з них та за допомогою вбудованої функції _asdict() вивести його як словник у консоль.
Fish = namedtuple('Fish',['name','species','tank'])
Gold= Fish('Goldy','Kapacb','3L')
Shark = Fish('Sharky','White Shark','Ocean')
Catfish = Fish('Mustache','Catfish','River')
set_fish = Shark
fish_dict = set_fish._asdict()
print(fish_dict)

#defaultdict: 
# Використовуючи один з варіантів namedtuple створити defaultdict 
# та задати йому відповідний тип даних
# (Згідно тому що маємо в namedtuple) для значень за замовчуванням.
def_fish_dict = defaultdict(Fish)


#deque:
# Створити відповідний пустий список deque, та показати як легко додати на початок,
# на кінець списку не використовуючи індексів,
# а також як легко видалити з обох кінців.
my_deque = deque()
print(my_deque)
my_deque.appendleft(1)
print(my_deque)
my_deque.append(3)
print(my_deque)
my_deque.pop()
print(my_deque)
my_deque.popleft()
print(my_deque)


#Декоратор. 
# Створити декоратор який буде виводити результат функції в консоль, 
# функція має щось повертати але не друкувати.
def my_decor(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper
