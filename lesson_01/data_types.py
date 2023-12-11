# import math
from math import sqrt

# Змінні
## None
var_none = None

## Boolean
var_true = True
var_true_ = 1

var_false = False
var_false_ = 0

## Numeric
var_int = 4
var_float = 7.5
var_complex = 2 + 4j

## Sequence
var_empty_list = []
var_list = [1, 2, 3]
var_empty_list_ = list()
var_empty_tuple = ()
var_empty_tuple_ = tuple()
var_tuple = (1, 2, 3)
var_range = range(1, 10, 2)

##Text Sequence
var_str = 'Hello World'
var_str2 = "Hello World"

# Binary Sequence
var_byte = bytes()

# Set
var_empty_set = set()
var_set = {1, 2, 3, 4, 4, 4, 5}
var_frozenset = frozenset(var_set)

# dict
var_empty_dict = {}
var_empty_dict_ = dict()
var_dict = {
    '1': 1,
    'list': var_list,
    'set': var_set,
    'bool': True
}


# Типи даних

# None - невизначене значення змінної.

# Boolean Type - логічний тип.

# Numeric Type - числа
## int - ціле число
## float - число з плаваючою точкою
## complex - комплексне число

# Sequence Type - послідовність
## list - список
## tuple - кортеж
## range - діапазон

# Text Sequence - текстова послідовність
## str - рядок

# Binary Sequence
## bytes - байти
## bytearray - масив байт
## memoryview - спеціальний об'єкт для доступу до внутнішніх даних об'єкта через protocol buffer

# Set - множина
## set - множина
## frozenset - незмінювана множина

# Mapping Types - словники
## dict


def print_var(variable):
    print('=' * 50)
    print(variable)


def print_variable(variable):
    print_var(variable)
    print(id(variable))
    print(type(variable))


if __name__ == "__main__":
    print_variable(var_none)
    print_variable(var_true)
    print_variable(var_false)
    print_variable(var_int)
    print_variable(var_float)
    print_variable(var_complex)
    print_variable(var_empty_list)
    print_variable(var_empty_list_)
    print_variable(var_list)
    print_variable(var_empty_tuple)
    print_variable(var_empty_tuple_)
    print_variable(var_tuple)
    print_variable(var_range)
    print_variable(var_range)
    print_variable(var_str)
    print_variable(var_str2)
    print_variable(var_byte)
    print_variable(var_empty_set)
    print_variable(var_set)
    print_variable(var_frozenset)
    print_variable(var_empty_dict)
    print_variable(var_empty_dict_)
    print_variable(var_dict)
    print_variable(isinstance(var_true, bool))

    ## Арифметика

    print_var(1 + 1)
    print_var(1 - 1)
    print_var(1 / 2)
    print_var(1 * 3)
    print_var(5 // 2)
    print_var(5 % 2)
    print_var(2**2)
    print_var(2**3)
    print_variable(sqrt(9))
    print_variable(sqrt(121))
    print_variable(sqrt(111))
