from math import sqrt, pow
import sys
import unittest
from math import isclose

class Calculator(unittest.TestCase):
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

        result_sub_1 = self.calc.subtract(1, 1)
        self.assertEqual(result_sub_1, 0)

        result_sub_2 = self.calc.subtract(-1, -1)
        self.assertEqual(result_sub_2, -2)

        result_sub_3 = self.calc.subtract(0, -1)
        self.assertEqual(result_sub_3, -1)

        result_sub_4 = self.calc.subtract(1.5, -1.5)
        self.assertEqual(result_sub_4, 0)
    def mult(self, a, b):
        return a * b

        result_mult_1 = self.calc.mult(0, 2)
        self.assertEqual(result_mult_1, 0)

        result_mult_2 = self.calc.mult(-1, 4)
        self.assertEqual(result_mult_2, -4)

        result_mult_3 = self.calc.mult(2, 0.5)
        self.assertEqual(result_mult_3, 1)

        result_mult_4 = self.calc.mult(0.5, 0.5)
        self.assertTrue(result_mult_4, 0.25)

    def div(self, a, b):
        return a / b

        result_div_1 = self.calc.div(9, 3)
        self.assertEqual(result_div_1, 3)

        result_div_2 = self.calc.div(0, 1)
        self.assertTrue(result_div_2, 0)

        result_div_3 = self.calc.div(0.25, 25)
        self.assertTrue(result_div_3, 0.01)

        with self.assertRaises(ValueError):
            self.calc.div(-1, 0)


    def power(self, a, b):
        return pow(a, b)
        result_power_1 = self.calc.power(2, 3)
        self.assertEqual(result_power_1, 8)

        result_power_2 = self.calc.power(5, 0)
        self.assertEqual(result_power_2, 1)

        result_power_3 = self.calc.power(4, -1)
        self.assertEqual(result_power_3, 0.25)

        result_power_4 = self.calc.power(1.5, 2)
        self.assertEqual(result_power_4, 2.25)

    def square_root(self, a):
        return sqrt(a)

        result_sqrt_1 = self.calc.square_root(64)
        self.assertEqual(result_sqrt_1, 8)

        with self.assertRaises(ValueError):
            self.calc.square_root(-25)

        result_sqrt_2 = self.calc.square_root(2.25)
        self.assertTrue(result_sqrt_2, 1.5)

if __name__ == "__main__":
    calc = Calculator()
    calc.add('2.0', '2')
    print(sys.platform)
    print(sys.version_info)
    print(sys.version)
    unittest.main()