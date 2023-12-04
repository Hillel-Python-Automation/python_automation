from math import sqrt, pow
import sys


class Calculator:
    def add(self, a, b):
        if isinstance(a, str):
            if a.isdigit():
                a = float(a)
            elif a.count('.') == 1:
                c = a.replace('.', '')
                if c.isdigit():
                    a = float(a)
        if isinstance(b, str) and b.isdigit():
            b = float(b)
        if not isinstance(a, int) and not isinstance(a, float):
            raise TypeError("Please use only next allowed types: int, float")
        return a + b

    def subsctract(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def power(self, a, b):
        return pow(a, b)

    def square_root(self, a):
        return sqrt(a)


if __name__ == "__main__":
    calc = Calculator()
    calc.add('2.0', '2')
    print(sys.platform)
    print(sys.version_info)
    print(sys.version)
