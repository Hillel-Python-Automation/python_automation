from functools import singledispatchmethod, singledispatch
from typing import Any


@singledispatch
def print_type(arg: Any):
    raise NotImplementedError(f"The current datatype: {type(arg)} in not supported")


@print_type.register
def _(arg: int | float):
    print(f"The argument of the function is a number and equal to {arg}")


@print_type.register(str)
def _(arg):
    print(f"The argument of the function is a string: {arg}")


class OverloadExample:
    @singledispatchmethod
    def class_type_print(self, arg: Any):
        print(f"The current datatype: {type(arg)} in not supported")

    @class_type_print.register
    def _(self, arg: int):
        print(f"Integer: {arg}")


if __name__ == "__main__":
    print_type(4)
    print_type(4.0)
    print_type('4')
    # print_type([1, 2, 3])

    _class = OverloadExample()
    _class.class_type_print(4)
    _class.class_type_print(None)

