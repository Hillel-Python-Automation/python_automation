print(dir())
from lesson_15 import map_vs_reduce as mr
print(dir())
from demo_wheel.hello import *
from lesson_15.classmethod_and_staticmethod import Person, People, Utils
print(dir())
import lesson_15
print(dir())


var = mr.flatten_list
print(var)
people = People('Yurii', 35)
print(people.__repr__())
person = Person('Yurii', 35)
print(person.get_person_details())
utils = Utils()
print(utils)
print(lesson_15.classmethod_and_staticmethod.Utils.is_palindrome('abba'))
print_hello()


