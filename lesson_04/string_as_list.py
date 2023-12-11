var = 'assdfhsdjkhksjdhfkjsdhfkjsdhfkj'

print(var[0])
print(var[10])
_var = var[10].replace('h', '?')
print(_var)
print(var)

print(type(var))

_list = list(var)
print(_list)
print(type(_list))
print('count of letter h', _list.count('h'))
print('index of the first letter h', _list.index('h'))
# print(_list.sort())
print(_list)


# slicing

print(var[3:7])
print(_list[3:7])
print(_list[:])
print(_list[3:]) # from the element 3 to the end
print(_list[:7]) # from beginning to element 6
print(_list[-1]) # last element
print(_list[-2])
print(_list[::-1])
print(_list.reverse())
print(_list)

print(var[::-1])
print(list(reversed(_list)))

print(_list)


