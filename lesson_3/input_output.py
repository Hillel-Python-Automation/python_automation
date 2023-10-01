# Вивід на консоль
print('Hello')

# Введення з консолі
## input повертає все введене з консолі як тип даних string
name = input('What is your name? ')
lastname = input('What is your lastname? ')
print(type(name))
print(type(lastname))
print('Hello', name, lastname)
print('Hello', name, lastname, sep=', ')
print('Hello', name, lastname, sep='\n', end='!\n')
print('Hello', name, lastname, sep='-', end='!\n')

if name.lower() == 'yurii':
    print('Long time no see')

# Приведення типів
## Cast

a = int(input('Enter a: '))
b = int(input('Enter b: '))

print(a - b)

a = str(a)
b = str(b)

print(a - b)
