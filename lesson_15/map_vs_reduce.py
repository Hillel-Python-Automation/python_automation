from functools import reduce

var1 = list(map(lambda x: x + x, range(11)))
print(var1)
var2 = list(map(float, range(11)))
print(var2)

var3 = reduce(lambda x, y: x < y, [1, 2, 5, 0, 6, 5])
print(var3)
# var4 = reduce(float, range(11))
# print(var4)


nested_list = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]

flatten_list = reduce(lambda x, y: x+y, nested_list)
print(flatten_list)
var_map = list(map(lambda x: str(x), nested_list))
print(var_map)

print(nested_list[0] + nested_list[1] + nested_list[2])
