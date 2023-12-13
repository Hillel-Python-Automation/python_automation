import unittest
from ..app.calc import Calculator
from parameterized import parameterized


class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('SetUpClass')
        cls._calc = Calculator()

    @classmethod
    def tearDownClass(cls):
        print('TearDownClass')

    def setUp(self):
        print('setUp')
        self.calc = self._calc
        print(id(self.calc))

    def tearDown(self):
        print('tearDown')
        del self.calc

    def test_add_2_plus_2(self):
        self.assertEqual(self.calc.add(2, 2), 4)

    @parameterized.expand([
        ('two plus two equals four', 2, 2, 4),
        ('-2 + -2 = -4', -2, -2, -4),
        ('2 + 0 = 2', 2, 0, 2),
    ])
    def test_add_functionality(self, _, a, b, expected_result):
        self.assertEqual(self.calc.add(a, b), expected_result)

    @parameterized.expand([
        ('2 * 2 = 4 ', 2, 2, 4),
        ('-2 * 0 = 0', -2, 0, 0),
        ('1 * 1 = 1', 1, 1, 1),
    ])
    def test_mult_functionality(self, _, a, b, expected_result):
        self.assertEqual(self.calc.mult(a, b), expected_result)

    @parameterized.expand([
        ('2 / 2 = 1 ', 2, 2, 1.0),
        ('-2 / 0 = ZeroDivisionError', -2, 0, ZeroDivisionError),
        ('1 / 1 = 1', 1, 1, 1.0),
    ])
    def test_div_functionality(self, _, a, b, expected_result):
        if b == 0:
            with self.assertRaises(expected_result):
                self.calc.div(a, b)
        else:
            self.assertEqual(self.calc.div(a, b), expected_result)

    @parameterized.expand([
        ('2 - 2 = 0', 2, 2, 0),
        ('-2 - 0 = 2', -2, 0, -2),
        ('-1 - 1 = -2', -1, 1, -2),
    ])
    def test_substract_functionality(self, _, a, b, expected_result):
        self.assertEqual(self.calc.substract(a, b), expected_result)

    @parameterized.expand([
        ('2 ** 2 = 0', 2, 2, 4),
        ('-2 ** 0 = 1', -2, 0, 1),
        ('-1 ** - 1 = -1', -1, -1, -1.0),
    ])
    def test_power_functionality(self, _, a, b, expected_result):
        self.assertEqual(self.calc.power(a, b), expected_result)

    @parameterized.expand([
        ('sqrt(4) = 2.0', 4, 2.0),
        ('sqrt(1) = 1.0', 1, 1.0),
        ('sqrt(0) = 0.0', 0, 0.0),
        ('sqrt(-4) = ValueError', -4, ValueError),
    ])
    def test_square_root_functionality(self, _, a, expected_result):
        if a < 0:
            with self.assertRaises(expected_result):
                self.calc.square_root(a)
        else:
            self.assertEqual(self.calc.square_root(a), expected_result)


if __name__ == '__main__':
    unittest.main()
