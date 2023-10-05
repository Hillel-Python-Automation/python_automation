import time

_list = [1, 2, 3, 4, 4, 56, 3, 2, 12, 4, 45, 3, 3, 2, 2, 21, 1]
start = time.perf_counter()
var_dict = {}
print('time dict {}', (time.perf_counter()-start)*1000)

start = time.perf_counter()
var_dict1 = dict()
print('time dict dict()', (time.perf_counter()-start)*1000)

print(var_dict)
print(var_dict1)
print(type(var_dict))
print(type(var_dict1))

var_dict2 = {
    'key': 'value'
}
print('one item dictionary', var_dict2)

var_dict3 = {
    '1': 10,
    '2': 20,
    '3': 30
}
print('multy items dictionary', var_dict3)

print(var_dict3['1'])
print(type(var_dict3['1']))
print(var_dict3.get('2'))
print(var_dict3.get('4'))

print('4' in var_dict3.keys())
print(var_dict3.values())

var_dict3['4'] = 40

print(var_dict3)

var_dict3.update({
    '5': 50,
    '6': 60
})

print(var_dict3)

var_dict3['7'] = var_dict2

print(var_dict3)

print(var_dict3['7']['key'])

var_dict3.update({
    '8': _list
})

print(var_dict3)

print(var_dict3.items())
print(var_dict3.pop('1'))
print(var_dict3)
print(var_dict3.popitem())
print(var_dict3)

var_dict3.update(var_dict2)

print(var_dict3)

for i in var_dict3:
    print(i, var_dict3.get(i))

for k, v in var_dict3.items():
    print(k, v)

#

