from functools import reduce

my_list = [1, 2.5, 3, 4.7, 5]

sum_list = reduce(lambda x, y: x + y, my_list)

print(sum_list)

from functools import reduce

list_of_lists = [[1,2,3], [3,4,5], [6,7,8]]

flat_list = reduce(lambda x,y: x+y, list_of_lists)

print(flat_list)

my_list = [1,2,3,4,5,6,7,8,9,10]

even_numbers = list(filter(lambda x: x%2 == 0, my_list))

print(even_numbers)

my_list = ['a', 'b', 'c', 'a', 'd', 'e', 'a']

a_elements = list(filter(lambda x: 'a' in x, my_list))

print(a_elements)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

zipped = list(zip(list1, list2))
print(zipped)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8]

zipped = list(zip(list1, list2, list3))
print(zipped)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 10
for i in range(n):
    print(fibonacci(i))

class PlaceHolder:
    pass


class Printer:
    def __init__(self, param):
        self.param = param

    def print(self):
        print(self.param)


x = Printer('Parameter')
x.print()