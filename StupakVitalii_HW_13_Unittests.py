from math import sqrt, pow
import sys
import unittest
from math import isclose
from parameterized import parameterized
import calculator

class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calc = TestCalculator()
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
    def test_add(self):
        self.assertEqual(self.calc.add(1, 1), 2)

        self.assertEqual(self.calc.add(31, 31), 62)

        self.assertEqual(self.calc.add(0, 0), 0)

        self.assertEqual(self.calc.add(1.5, 1.5), 3)

    def subtract(self, a, b):
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
        return a - b

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 1), 0)

        self.assertEqual(self.calc.subtract(31, 31), 0)

        self.assertEqual(self.calc.subtract(4, 2), 2)

        self.assertEqual(self.calc.subtract(1.5, 1.5), 0)

    def mult(self, a, b):
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
        return a * b

    def test_mult(self):

        self.assertEqual(self.calc.mult(2, 2), 4)

        self.assertEqual(self.calc.mult(-1, 2), -2)

        self.assertEqual(self.calc.mult(2, 0.5), 1)

        self.assertEqual(self.calc.mult(0.5, 0.5), 0.25)

    def div(self, a, b):
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
        return a / b

    def test_div(self):

            self.assertEqual(self.calc.mult(9, 3), 27)

            self.assertEqual(self.calc.mult(0, 1), 0)

            self.assertEqual(self.calc.mult(0.25, 25), 6.25)

    def pow(self, a, b):
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
        return pow(a,b)

    def test_pow(self):

            self.assertEqual(self.calc.pow(2, 3), 8)

            self.assertEqual(self.calc.pow(2,2 ), 4)

            self.assertEqual(self.calc.pow(3, 2), 9)

            self.assertEqual(self.calc.pow(3, 3), 27)


    def sqrt(self,a):
        if isinstance(a, str):
            if a.isdigit():
                a = float(a)
            elif a.count('.') == 1:
                c = a.replace('.', '')
                if c.isdigit():
                    a = float(a)

        if not isinstance(a, int) and not isinstance(a, float):
            raise TypeError("Please use only next allowed types: int, float")
        return sqrt(a)

    def test_sqrt(self, a):

            self.assertEqual(self.calc.sqrt(4), 2)

            self.assertEqual(self.calc.sqrt(0), 0)

            self.assertEqual(self.calc.sqrt(1), 1)

            self.assertEqual(self.calc.sqrt(-4), 2)


if __name__ == "__main__":
    calc = TestCalculator()
    calc.add('2.0', '2')
    print(sys.platform)
    print(sys.version_info)
    print(sys.version)
    unittest.main()
