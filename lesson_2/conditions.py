# if condition:
#     expression

a = 6
b = 4
none = True
var_float = 7.5
var_string = 'hi'
var_string_decimal = '34'

if a < b:
    print('a < b')

if a > b:
    print('a > b')
else:
    print('a < b')

if a < b:
    print('a < b')
elif a > b:
    print('a > b')
elif a > b:
    print('3 a == b')
else:
    print('no one condition is true')

## Nested if (Вкладені if)


if a > b:
    if a > 6:
        print('nested if: a > b and a > 6')
    else:
        print('nested if: a > b and a <= 6')

##

if a < b:
    if a <= 5:
        if a == b:
            print('a < b')

elif a > b:
    print('a > b')
elif a > b:
    print('3 a == b')
else:
    print('no one condition is true')

if isinstance(a, int):
    print('a is int')
if none is None:
    print('none is None')
if isinstance(var_string, str):
    print(var_string, type(var_string))

if var_string_decimal.isdigit():
    print(var_string_decimal)
    print(type(var_string_decimal))
    var_string_decimal = int(var_string_decimal)
    print(var_string_decimal)
    print(type(var_string_decimal))

## Оператори для перевірки умов

if a > b:
    print(a)
if a >= b:
    print(a)
if a < b:
    print(b)
if a <= b:
    print(b)
if a == b:
    print(a)
if a != b:
    print(a)
if none is None:
    print(none)
if isinstance(var_string, str):
    print(var_string)

if not none:
    print('something')
if none is not None:
    print('something in is not None')

## Декілька умов

if a > b and a > 3:
    print(a)
if (a > b or a > 30) and b % 2 == 0:
    print('OR')

if var_string == 'hi':
    print(var_string)

###### match-case

command = "hello"

match command.lower():
    case 'hi':
        print('hi to you')
    case 'good morning':
        print('Good Morning to you too')
    case 'hello' | 'hellou' | 'Hello':
        print('Hello to you')
    case 'wazzup':
        print('Wazzup')
    case _:
        print('I don\'t understand you')

if command == 'hi':
    print('hi to you')
elif command == 'good morning':
    print('Good Morning to you too')
elif command in ('hello', 'hellou', 'Hello'):
    print('Hello to you')
elif command == 'Wazzup':
    print('Wazzup')
else:
    print('I don\'t understand you')


digit = 0
_string = '0'

if _string == '0':
    print(_string)

if digit != 0:
    print('digit is not equal to zero')
else:
    print('digit is equal to zero')


if _string != '0':
    print('_string is not equal to zero')
else:
    print('_string is equal to zero')

if 0 == _string:
    pass
