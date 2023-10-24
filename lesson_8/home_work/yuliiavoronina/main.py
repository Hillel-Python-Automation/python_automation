# Counter: Дано рядок у вигляді випадкової послідовності чисел від 0 до 9. Потрібно створити словник,
# який як ключі прийматиме дані числа (тобто ключі будуть типом int), а як значення – кількість цих чисел
# у наявній послідовності. Для побудови словника створіть функцію count_it(sequence), що приймає рядок
# із цифр. Функція повинна повернути словник з трьох найчастіше зустрічаються чисел.
from collections import Counter, namedtuple, defaultdict, deque

base = [0, 1, 3, 5, 7, 9, 9, 5, 9, 3, 6, 3, 9, 0, 3, 2, 2, 7, 7, 7, 7, 5, 8, 9]


def count_it(sequence):
    c = Counter(sequence)
    return c.most_common(3)


print(count_it(base))

# namedtuple: Створити namedtuple з іменем Fish та іменними аргументами "name", "species", "tank". Створити
# кілька об'єктів такого namedtuple. Вибрати один з них та за допомогою вбудованої функції _asdict() вивести
# його як словник у консоль.
Fish = namedtuple("Fish", ["name", "species", "tank"])

fish1 = Fish("Bleeding heart tetra", "Hyphessobrycon erythrostigma", 6.5)
fish2 = Fish("Red phantom tetra", "Hyphessobrycon sweglesi", 4.5)
fish3 = Fish("Flameback", "Pundamilia nyererei", 10)
fish4 = Fish("Flowerhorn cichlid", "Cichlasoma sp.", 25)
fish5 = Fish("Bluefin Notho", "Nothobranchius rachovii", 6)
fish6 = Fish("Siamese fighting fish", "Betta splendens", 7.5)

print(fish1._asdict())

# defaultdict: Використовуючи один з варіантів namedtuple створити defaultdict та задати йому відповідний
# тип даних (Згідно тому що маємо в namedtuple) для значень за замовчуванням.

converted = fish5._asdict()

print("converted", converted)

d = defaultdict(Fish, converted)

print("defaultdict", d)

# deque: Створити відповідний пустий список deque, та показати як легко додати на початок, на кінець списку
# не використовуючи індексів, а також як легко видалити з обох кінців.

d = deque()
print(d)

d.appendleft('f')
d.append('l')
print(d)
d.pop()
d.popleft()
print(d)

# Декоратор. Створити декоратор який буде виводити результат функції в консоль, функція має щось повертати але
# не друкувати.
# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators


def wrapper(f):
    def fun(l):
        res = []
        l = l.split("\n")
        for i in range(len(l)):
            l[i] = l[i].lstrip()
        for i in range(1,len(l)):
            if len(l[i]) == 10:
                res.append("+91 " + l[i][:5] + " " + l[i][5:])
            elif len(l[i]) == 11:
                res.append("+91 " + l[i][1:6] + " " + l[i][6:])
            elif len(l[i]) == 12:
                res.append("+91 " + l[i][2:7] + " " + l[i][7:])
            else:
                res.append("+91 " + l[i][3:8] + " " + l[i][8:])
        f(res)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = """3
            07895462130
            919875641230
            9195969878"""
    sort_phone(l)
