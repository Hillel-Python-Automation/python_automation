# x, y = y, x
#
# tmp = x
# x = y
# y = tmp

file = open("text2.txt", 'w')
file.write('Hello, Python!')
file.close()

file = None

try:
    file = open("text2.txt", 'r')
    content = file.read()
    print(content)
    # file.write('Hello, Python!\n')
except FileExistsError as e:
    print(e)
finally:
    file.close()

# try:
#     file = open("testfile2.png", 'rb')
#     content = file.read()
#     print(content)
#     # file.write('Hello, Python!\n')
# except FileExistsError as e:
#     print(e)
#
# finally:
#     file.close()


# Context manager

with open('text3.txt', 'w') as fl:
    fl.write("Hello from context manager")

with open('text3.txt') as fl:
    print(fl.read())

print('Hello after context manager')
