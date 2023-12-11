import copy

_list = [1, 2, 3, 4, 5, 6, 7, 8]

_list2 = [1, "3", 'three']

_list3 = [_list, _list2]

print(_list)
print(_list2)
print(_list3)

print(len(_list))
print(len(_list2))
print(len(_list3))

print(_list3[0])

print(_list == _list3[0])

_list3[0][0] = 10

print(_list3)
print(_list)

_list[-1] = 9

print(_list3)
print(_list)

# Copying the lists
print(13 * '_')
_shallow_copy = _list

print(id(_shallow_copy))
print(_shallow_copy)
print(id(_list))
print(_list)


_hard_copy = _list.copy()
print(id(_hard_copy))
print(_hard_copy)
print(id(_list))
print(_list)


_hard_copy_list = copy.copy(_list3)
_deep_copy = copy.deepcopy(_list3)

print('_list3')
print(id(_list3))
print(id(_list3[0]))
print(id(_list3[1]))
print('_hard_copy_list')
print(id(_hard_copy_list))
print(id(_hard_copy_list[0]))
print(id(_hard_copy_list[1]))
print('_deep_copy')
print(id(_deep_copy))
print(id(_deep_copy[0]))
print(id(_deep_copy[1]))

# lists

print(_list.index(3))

print(_list.count(3))

print(_list.sort(reverse=True))
print(_list)
print(_list.extend(_list2))
print(_list)
_list.append(_list2)
print(_list)
_list.insert(9, 0)
print(_list)

_list.remove('3')
print(_list)

print(_list.pop())
print(_list)
print(_list.pop(0))
print(_list)

del _list[2]
print(_list)

_list.clear()
print(_list)

del _list

print(_list)

