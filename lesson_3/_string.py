import string as st

print(type(''))
print(type(""))

print('', end='!')
print("", end='!\n')

greetings = 'Hello Hello'
uppercase = "HELLO HELLO"
lowercase = 'hello hello'
case = 'HeLLo HeLLo'

# Операції над рядками
print(3*'-', 'Lower', 3*'-')
print(greetings.lower())
print(uppercase.lower())
print(lowercase.lower())
print(case.lower())

print('Upper')
print(greetings.upper())
print(uppercase.upper())
print(lowercase.upper())
print(case.upper())
print('Title')
print(greetings.title())
print(uppercase.title())
print(lowercase.title())
print(case.title())
print('Capitalize')
print(greetings.capitalize())
print(uppercase.capitalize())
print(lowercase.capitalize())
print(case.capitalize())
print('Casefold')
print(greetings.casefold())
print(uppercase.casefold())
print(lowercase.casefold())
print(case.casefold())
print('Swapcase')
print(greetings.swapcase())
print(uppercase.swapcase())
print(lowercase.swapcase())
print(case.swapcase())

print(greetings.encode(encoding='UTF-8'))

# Перевірки
print('Is digit')
print('12345'.isdigit())
print('123.45'.isdigit())
print('123.45'.isdecimal())
print('12345a'.isdigit())
print('12345a'.isalnum())
print('12345a'.isalpha())
print('sdfsdfa'.isalpha())
print(' '.isspace())
print('Count')
print('cvcv xcxcv'.count(' ') > 0)
print('cvcv xcxcv'.index(' '))
print("aasdas asdasd asdasd".index(' '))
print("aasdas asdasd asdasd".rindex(' '))
print("aasdas asdasd asdasd".count(' '))

_string = "aasdas asdasd asdasd"

for i, char in enumerate(_string):
    if char == ' ':
        print(i)

print('Split')
_list = _string.split(' ')
print(_list)

print('Join')
print(', '.join(_list))

print('Replace')
print(_string.replace('a', 'y'))
print(_string.replace(' ', '-'))
print(_string.replace(' ', ', '))

print('Strip')

print(' dshfsjdh ')
print(' dshfsjdh '.strip())
print(' dshfsjdh '.lstrip())
print(' dshfsjdh '.rstrip())
print(' dshfsjdh '.strip('h'))


### Format string
print("Format string")
output = 'sbfjh ' + str(45) + ' sdfsdf'
print(output)

age = 34
text = 'My age is {0} ${1}'.format(age, output.capitalize())
text2 = f"My age is {age:.4f} ${output.capitalize()}"
text3 = r"c:\\Windows\\Users\\Yurii\'"
text6 = "c:\\Windows\\Users\\Yurii\\"
text4 = r"hello\nworld"
text5 = 'hello\\nworld'

text8 = "М'ясо"
text7 = 'М\'ясо'

multiline = """
    Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""

_multiline = '''
    Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''

print(text)

print(text2)

print(text3)
print(text4)
print(text5)
print(text6)

print(int('45'))
print(float('45.5'))


print(multiline)
print(_multiline)

print(st.digits)
print(st.ascii_lowercase)
print(st.ascii_uppercase)

