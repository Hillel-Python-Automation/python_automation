var_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

var_new_list = []
for item in var_list:
    if item % 2 == 0:
        var_new_list.append(item)

print(var_new_list)

var_even_elements = [item for item in var_list if item % 2 == 0]
print(var_even_elements)

var_for_list = []
for x in var_list:
    var_for_list.append(x ** 2)

print(var_for_list)

var_new_list2 = [item ** 2 for item in var_list]

print(var_new_list2)

var_list_if_else = []
for x in var_list:
    if x % 2 == 0:
        var_list_if_else.append(x ** 2)
    else:
        var_list_if_else.append(x * 2)

print(var_list_if_else)

var_list_if_else_comprehension = [x ** 2 if x % 2 == 0 else x * 2 for x in var_list]
print(var_list_if_else_comprehension)

var_dict = {
    'Ford': 1984,
    'Mustang': 1964,
    'Cadillac': 1973,
    'Maseratti': 2020
}

var_list_keys_comprehension = [item.upper() for item in var_dict.keys() if item.startswith('M')]
print(var_list_keys_comprehension)

var_list_keys = []
for item in var_dict.keys():
    if item.startswith('M'):
        var_list_keys.append(item.upper())

print(var_list_keys)

var_list_example = [1, 2, 3]

print(var_dict.keys())
print(var_dict.values())
print(var_dict.items())

dict_comprehension = {k.upper(): str(v) for k, v in var_dict.items()}
print(type(dict_comprehension))
print(dict_comprehension)

## MAP

str_list = list(map(str, var_list))
print(str_list)


def addition(n):
    return n + n


mapped_list = list(map(addition, var_list))
print(mapped_list)

lambda_mapped_list = list(map(lambda x: x + x, var_list))
print(lambda_mapped_list)

comprehension_list = [i + i for i in var_list]
print(comprehension_list)

for_list = []
for i in var_list:
    for_list.append(i + i)
print(for_list)

## ZIP

zipped_list = zip(var_list, str_list)
print(id(zipped_list))
zipped_list_ = list(zipped_list)
print(id(zipped_list_))
print(id(zipped_list))
print(tuple(zipped_list_))

comprehension_list.pop()
triple_zipped_list = zip(var_list, str_list, comprehension_list)
print(list(triple_zipped_list))

for_zipped_list = []
length = min(len(var_list), len(str_list), len(comprehension_list))
for i in range(length):
    for_zipped_list.append((var_list[i], str_list[i], comprehension_list[i]))

print(for_zipped_list)


## Filter


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


evens = filter(is_even, var_list)
lambda_evens = filter(lambda x: True if x % 2 == 0 else False, var_list)
print(evens)

# for e in evens:
#     print(e)

print(list(evens))
print(list(lambda_evens))
