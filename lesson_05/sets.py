var_set = set()

print(var_set)
print(type(var_set))

# Set - множина яка містить тільки унікальні дані
var_set2 = {1, 4, 2, 3, 4}
print(var_set2)
print(type(var_set2))

var_set3 = {'a', 'c', 'd', 'f', 'e'}
var_set5 = {'a', 'c', 'x'}
var_set6 = {'e', 'y'}

print(var_set3)

varset4 = {}
print(type(varset4))
print(varset4)

# Доступ до елементів множини

print('a' in var_set3)

for i in var_set3:
    print(i)

print('superset', var_set3.issuperset(var_set5))   # var_set3 = {'a', 'c', 'd', 'f', 'e'}  var_set5 = {'a', 'c'}  -> TRUE
print('subset', var_set5.issubset(var_set3))     # var_set5 = {'a', 'c'} var_set3 = {'a', 'c', 'd', 'f', 'e'} -> TRUE
print('disjoint', var_set3.isdisjoint(var_set6))   # var_set3 = {'a', 'c', 'd', 'f', 'e'} var_set6 = {'e', 'y'} -> FALSE -> 'e'
print('difference', var_set3.difference(var_set5))   # var_set3 = {'a', 'c', 'd', 'f', 'e'}  var_set5 = {'a', 'c'} -> {'d', 'f', 'e'}
print('intersection', var_set3.intersection(var_set5))  # var_set3 = {'a', 'c', 'd', 'f', 'e'}  var_set5 = {'a', 'c'} -> {'a', 'c'}
print('symmetric difference', var_set3.symmetric_difference(var_set5))  # var_set3 = {'a', 'c', 'd', 'f', 'e'}  var_set5 = {'a', 'c'} -> {'d', 'f', 'e'}
print(var_set3 ^ var_set5)
print('union', var_set3.union(var_set5))
print(var_set3 | var_set5)


print(var_set3)
var_set3.add('a')
print(f"add a {var_set3}")
var_set3.add('y')
print(f"add y {var_set3}")
var_set3.remove('a')
print(f"remove a {var_set3}")
var_set3.discard('y')
print(f"discard y {var_set3}")
var_set3.discard('y')
print(f"discard y {var_set3}")
# var_set3.remove('a')
# print(f"remove a {var_set3}")

print(var_set3.pop())

print(var_set3.difference(var_set5))
print(var_set3.difference_update(var_set5))
print(var_set3)


_list = [1, 2, 3, 4, 4, 56, 3, 2, 12, 4, 45, 3, 3, 2, 2, 21, 1]

print(_list)

print('List length: ', len(_list))


temp_var = []
for i in _list:
    print(i)
    if i not in temp_var:
        temp_var.append(i)
print(temp_var)
print('Unique items:', len(temp_var))

print('Unique items count using set:', len(set(_list)))
var_set3.add('e')
var_set5.add('e')
print('set3', var_set3, 'set5', var_set5)
print(var_set3.symmetric_difference(var_set5))
print(var_set3.difference(var_set5))
print(var_set3.union(var_set5))


var_frozenset = frozenset(var_set3)

print(var_frozenset)
print(type(var_frozenset))
