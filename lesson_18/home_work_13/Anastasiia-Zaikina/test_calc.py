import unittest
from lesson_18.app.calc import Calculator
from parameterized import parameterized


class TestMult(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def tearDown(self):
        del self.calc

    @parameterized.expand([
        ('3 * 0 = 0', 3, 0, 0),
        ('2 * 2 = 4', 2, 2, 4),
        ('(-2) * (-3) = 6', -2, -3, 6),
        ('(-2) * 4 = (-8)', -2, 4, -8)
    ])
    def test_mult(self, description, first_value, second_value, expected_result):
        self.assertEqual(self.calc.mult(first_value, second_value), expected_result)

    @parameterized.expand([
        ('2 / 0 = ZeroDivisionError', 2, 0, ZeroDivisionError),
        ('0 / 2 = 0', 0, 2, 0),
        ('(-6) / (-2) = 3', -6, -2, 3),
        ('(-4) / 2 = -2', -4, 2, -2)
    ])
    def test_division(self, description, first_value, second_value, expected_result):
        if second_value == 0:
            with self.assertRaises(expected_result):
                self.calc.div(first_value, second_value)
        else:
            self.assertEqual(self.calc.div(first_value, second_value), expected_result)

    @parameterized.expand([
        ('2 - 2 = 0', 2, 2, 0),
        ('(-3) - (-3) = 0', -3, -3, 0),
        ('(-2) - 4 = -6', -2, 4, -6),
        ('6 - (-2) = 8', 6, -2, 8)

    ])
    def test_subtract(self, description, first_value, second_value, expected_result):
        self.assertEqual(self.calc.substract(first_value, second_value), expected_result)

    @parameterized.expand([
        ('2 ** 6 = 64', 2, 6, 64),
        ('4 ** 0 = 1', 4, 0, 1),
        ('0 ** 8 = 0', 0, 8, 0),
        ('2 ** (-2) = 0,25', 2, -2, 0.25)

    ])
    def test_power(self, description, first_value, second_value, expected_result):
        self.assertEqual(self.calc.power(first_value, second_value), expected_result)

    @parameterized.expand([
        ('sqrt(25) = 5', 25, 5),
        ('sqrt(1) = 1', 1, 1),
        ('sqrt(0) = 0', 0, 0),
        ('sqrt(-5) = ValueError', -5, ValueError)
    ])
    def test_square_root(self, description, value, expected_result):
        if value < 0:
            with self.assertRaises(expected_result):
                self.calc.square_root(value)
        else:
            self.assertEqual(self.calc.square_root(value), expected_result)


if __name__ == '__main__':
    unittest.main
