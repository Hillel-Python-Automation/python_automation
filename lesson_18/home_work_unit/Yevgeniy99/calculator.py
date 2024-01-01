from math import sqrt, pow
import sys
import unittest

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

    def subtract(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def power(self, a, b):
        return pow(a, b)

    def square_root(self, a):
        return sqrt(abs(a))


if __name__ == "__main__":
    calc = Calculator()
    calc.add('2.0', '2')
    print(sys.platform)
    print(sys.version_info)
    print(sys.version)


class TestCalculator(unittest.TestCase):

    def test_mult(self):
        calc = Calculator()

        self.assertEqual(calc.mult(2, 4), 8)
        self.assertEqual(calc.mult(5, 3), 15)
        self.assertEqual(calc.mult(-2, 3), -6)
        self.assertEqual(calc.mult(-4, 5), -20)

    def test_div(self):
        calc = Calculator()

        self.assertEqual(calc.div(15, 3), 5)
        self.assertEqual(calc.div(2.5, 3), 0.8333333333333334)
        self.assertEqual(calc.div(-3, 3), -1)
        self.assertEqual(calc.div(-2.5, 3), -0.8333333333333334)

    def test_subtract(self):
        calc = Calculator()

        self.assertEqual(calc.subtract(2, 3), -1)
        self.assertEqual(calc.subtract(2.5, 3), -0.5)
        self.assertEqual(calc.subtract(-2, 3), -5)
        self.assertEqual(calc.subtract(-2.5, 3), -5.5)

    def test_power(self):
        calc = Calculator()

        self.assertEqual(calc.power(2, 3), 8)
        self.assertEqual(calc.power(2.5, 3), 15.625)
        self.assertEqual(calc.power(-2, 3), -8)
        self.assertEqual(calc.power(-2.5, 3), -15.625)

    def test_square_root(self):
        calc = Calculator()

        self.assertEqual(calc.square_root(4), 2)
        self.assertEqual(calc.square_root(9), 3)
        self.assertEqual(calc.square_root(-16), 4)
        self.assertEqual(calc.square_root(-25), -5)


if __name__ == "__main__":
    unittest.main()