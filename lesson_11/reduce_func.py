from functools import reduce

var_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

var_reduce = reduce(lambda a, b: a+b, var_list)
print(var_reduce)

print(sum(var_list))

var_sum = 0
for i in var_list:
    var_sum += i
print(var_sum)

var_max = reduce(lambda a, b: a if a > b else b, var_list)
print(var_max)
print(max(var_list))
for_max = var_list[0]
for index, item in enumerate(var_list):
    if for_max < var_list[index]:
        for_max = var_list[index]
print(for_max)

for_max = var_list[0]
for i in range(1, len(var_list)):
    if for_max < var_list[i]:
        for_max = var_list[i]
print(for_max)

for_max = var_list[0]
for i in var_list:
    if for_max < i:
        for_max = i
print(for_max)


var_min = reduce(lambda a, b: a if a < b else b, var_list)
print(var_min)
print(min(var_list))

for_min = var_list[0]
for i in var_list:
    if for_min > i:
        for_min = i
print(for_min)

