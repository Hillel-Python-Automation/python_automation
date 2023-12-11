var = 'assdfhsdjkhksjdhfkjsdhfkjsdhfkj'

_list = [1, 2, 3, 4, 5, 6, 7, 8]

for item in _list:
    print("iteration")
    print(item)


for index in range(len(_list)):
    print(_list[index])

print(30 * '_')

for index, item in enumerate(_list):
    print(f"{index}: {item}")

for item in _list:
    if item % 2 == 0:
        print(f"the {item} is even")
    else:
        print(f"The {item} is odd")
else:
    print('The loop is ended')


for item in _list:
    if item == 4:
        print(_list.index(item))
        break
else:
    print('The loop is ended with break')

print(30 * '_')

for item in _list:
    if item < 5:
        continue
    else:
        print(item)
    print('the item is greater then 5')
else:
    print('The loop is ended')

print(30 * '_')

for i in range(10):
    print(f"i: {i}")
    for j in range(10):
        print(f"j: {j}")

for i in range(10):
    for j in range(i + 1):
        print("* ", end="")
    print("\r")
