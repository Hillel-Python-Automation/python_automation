# Функції які нічого не приймають і не реалізовані
from typing import overload


def function_name():
    ...


def function_name_1():
    pass


def function_name_2():
    return NotImplemented


# Функції які нічого не повертають
def print_greetings():
    print('Hello, world!')


# Функції які повертають значення

def return_text():
    return "Hello, world!"


def return_tuple_of_three():
    return 1, 2, 3


# Функції які приймають аргументи

def function_with_one_argument(a):
    print("This is the argument: {}".format(a))


def func_with_2_args(arg1, arg2):
    return arg1 * arg2


# Функція з багатьма аргументами
def func_with_many_args(*args):
    print(args)
    for arg in args:
        print(arg)


def func_with_kwargs(**kwargs):
    print(kwargs)
    for item in kwargs:
        print(item)
        print(kwargs.get(item))


def func_with_arg_default(arg1='*', arg2=50):
    print(arg1 * arg2)


def func_with_mixed_args(arg1='*', arg2=50, *args, **kwargs):
    print(arg1 * arg2)


def func_with_mixed_args_(*args, arg1='*', arg2,  **kwargs):
    print(arg1 * arg2)


def func_with_mixed_args__(arg1='*', arg2=50, *args,  **kwargs):
    print(args)
    print(kwargs)
    print(arg1 * arg2)


def func_with_type_checking(arg1: str, arg2: int = 50) -> None:
    print(arg1 * arg2)


def func_return_float(arg1: int, arg2: int) -> float:
    """
    Function multiply to ints and return float value
    :param arg1:
    :param arg2:
    :return: float -> multiplication of input args
    """
    if isinstance(arg1, int):
        pass
    elif isinstance(arg1, float):
        pass
    elif isinstance(arg1, object):
        pass
    else:
        raise Exception

    return float(arg1 * arg2)


def func_return_int(arg1: float, arg2: float) -> int:
    return int(arg1 * arg2)


def func_with_func():
    def nested_function():
        return 'Nested function'
    return nested_function


if __name__ == "__main__":
    function_name()
    print(function_name())
    function_name_1()
    print(function_name_1())
    function_name_2()
    print(function_name_2())

    print_greetings()
    print(print_greetings())

    return_text()
    print(return_text())

    print(return_tuple_of_three())
    x, y, z = return_tuple_of_three()
    print(x, y, z, sep=" ,")
    print(x)
    print(y)
    print(z)

    # Передача аргумента функції за значенням
    function_with_one_argument(5)
    # function_with_one_argument(input("Input your argument: "))
    # Передача аргумента за посиланням (передача змінної як аргумента)
    a = 10
    function_with_one_argument(a)
    # arg = input("Input your argument: ")
    # function_with_one_argument(arg)
    # arg = int(arg)
    # arg = arg / 100

    # print(arg)

    # function_with_one_argument(a=arg)

    print(func_with_2_args('*', 50))
    print(func_with_2_args('-', 50))
    print(func_with_2_args('+', 50))

    func_with_many_args(1)
    print(func_with_2_args('-', 50))
    func_with_many_args(1, 2)
    print(func_with_2_args('-', 50))
    func_with_many_args(1, 2, 3, 4, 5, 6, 7, 8, 9)

    print(func_with_2_args('-', 50))
    func_with_kwargs(arg1=2, name='Yurii', lastname='LASTNAME', age=34)

    func_with_arg_default()
    func_with_arg_default(arg1="=")
    func_with_arg_default(arg2=100)
    func_with_arg_default(arg1='+', arg2=1000)
    func_with_mixed_args()

    print(func_return_float(10, 10))
    print(type(func_return_float(10, 10)))

    print(func_return_float(10.4, 10.4))
    print(type(func_return_float(10.4, 10.4)))

    print(func_return_int(10.4, 10.3))
    print(type(func_return_int(10.4, 10.3)))

    print(func_return_float(4, 5))
    print(func_return_float(arg2=5, arg1=4))
    # func_return_float(arg2=5, 4)
    # func_return_float(arg1=4, 5)
    func_return_float(4, arg2=5)

    func_with_mixed_args_(1, 2, 3, 45, 5, arg1="3", arg2=3, name='function')
    func_with_mixed_args__("1", 2, 3, 45, 5, name='function')

    print(func_with_func()())
