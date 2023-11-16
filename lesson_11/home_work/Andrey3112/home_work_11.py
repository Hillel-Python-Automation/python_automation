### Reduce
#1)
from functools import reduce

var_list = [1, 2.1, 3.5, 7, 9, 8.5]
var_sum = reduce(lambda a, b: a + b, var_list)
print(var_sum)

#2)
list_1 = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
list_2 = reduce(lambda a, b: a + b, list_1)
print(list_2)


### Filter
#1)
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = list(filter(lambda a: a % 2 == 0, list_1))
print(list_2)

#2)
list_1 = ["Hello", "my", "dear", "friend"]
list_2 = list(filter(lambda a: "a" in a, list_1))
print(list_2)


### Zip
#1)
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = zip(list_1, list_2)
print(list(list_3))

#2)
list_1 = [1, 2, 3]
list_2 = [4, 5, 6, 7]
list_3 = [8, 9, 10, 11, 12]
list_4 = zip(list_1, list_2, list_3)
print(list(list_4))

### Recursion

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        posledovatelnost = fibonacci(n - 1)
        posledovatelnost.append(posledovatelnost[-1] + posledovatelnost[-2])
        return posledovatelnost
print(fibonacci(13))


### Class
#1)
class PlaceHolder:
    pass

#2)
class New_class:
    def __init__(self, name):
        self.name = name
Andrey_K = New_class("Andrey")
print(Andrey_K.name)