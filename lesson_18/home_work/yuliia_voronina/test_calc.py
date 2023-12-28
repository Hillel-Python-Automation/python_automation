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

    # mult test old
    def test_mult_2_3(self):
        self.assertEqual(self.calc.mult(2, 3), 6)

    def test_mult_2_0(self):
        self.assertEqual(self.calc.mult(2, 0), 0)

    def test_mult_str_str(self):
        with self.assertRaises(TypeError):
            exected = "Not a number"
            self.assertEqual(self.calc.mult('a', 'a'), exected)

    def test_mult_positive_on_negative(self):
        self.assertEqual(self.calc.mult(2, -2), -4)

    def test_mult_negative_on_negative(self):
        self.assertEqual(self.calc.mult(-2, -2), 4)

    def test_mult_float_int(self):
        expected = 6.3
        actual = self.calc.mult(2.1, 3)
        self.assertEqual(round(actual, 1), expected)

    def test_mult_float_float(self):
        expected = 5.8
        actual = self.calc.mult(2.3, 2.5)
        self.assertEqual(round(actual, 1), expected)

    # mult test new
    def test_mult_2_fraction1_2(self):
        self.assertEqual(self.calc.mult(2, 2 ** (-1)), 1)

    def test_mult_2_str(self):
        with self.assertRaises(TypeError):
            exected = "Not a number"
            self.assertEqual(self.calc.mult(2, 'a'), exected)

    def test_mult_negative_on_positive(self):
        self.assertEqual(self.calc.mult(-8, 2), -16)

    def test_mult_0_5(self):
        self.assertEqual(self.calc.mult(0, 5), 0)

    #division test old
    def test_div_6_3(self):
        expected = 2
        actual = self.calc.div(6, 3)
        self.assertEqual(actual, expected)

    def test_div_3_6(self):
        expected = 0.5
        actual = self.calc.div(3, 6)
        self.assertEqual(actual, expected)

    def test_div_on_zero(self):
        with self.assertRaises(ZeroDivisionError):
            expected = "not a number"
            actual = self.calc.div(3, 0)
            self.assertEqual(actual, expected)

    def test_div_zero_on_int(self):
        expected = 0
        actual = self.calc.div(0, 3)
        self.assertEqual(actual, expected)

    def test_div_int_on_str(self):
        with self.assertRaises(TypeError):
            expected = "not a number"
            actual = self.calc.div(1, "str")
            self.assertEqual(actual, expected)

    #division test new
    def test_div_str_on_float(self):
        with self.assertRaises(TypeError):
            expected = "not a number"
            actual = self.calc.div("str", 1.1)
            self.assertEqual(actual, expected)

    def test_div_int_on_float(self):
        with self.assertRaises(TypeError):
            expected = 0.4
            actual = self.calc.div(1, 2.5)
            self.assertEqual(actual, expected)

    def test_div_float_on_int(self):
        with self.assertRaises(TypeError):
            expected = 3.75
            actual = self.calc.div(7.5, 2)
            self.assertEqual(actual, expected)

    def test_div_float_on_float(self):
        with self.assertRaises(TypeError):
            expected = 2
            actual = self.calc.div(8.8, 4.4)
            self.assertEqual(actual, expected)

    # sub test old
    def test_sub_5_1_positive(self):
        actual = 4
        expected = self.calc.substract(5, 1)
        self.assertEqual(expected, actual)

    def test_sub_1_5_negative(self):
        actual = -4
        expected = self.calc.substract(1, 5)
        self.assertEqual(expected, actual)

    def test_sub_floats(self):
        expected = 1.1
        actual = self.calc.substract(5.5, 4.4)
        actual = round(actual, 1)
        self.assertEqual(actual, expected)

    def test_sub_int_float(self):
        expected = 1.9
        actual = self.calc.substract(5, 3.1)
        self.assertEqual(actual, expected)

    def test_sub_int_str(self):
        with self.assertRaises(TypeError):
            expected = "not a number"
            actual = self.calc.substract(10, "str")
            self.assertEqual(actual, expected)

    # sub test new
    def test_sub_negative_bigger_negative(self):
        actual = 4
        expected = self.calc.substract(-1, -5)
        self.assertEqual(expected, actual)

    def test_bigger_negative_negative(self):
        expected = -1.1
        actual = self.calc.substract(-5.5, -4.4)
        actual = round(actual, 1)
        self.assertEqual(actual, expected)

    def test_sub_float_int(self):
        expected = 2.8
        actual = self.calc.substract(5.9, 3.1)
        self.assertEqual(actual, expected)

    def test_sub_str_int(self):
        with self.assertRaises(TypeError):
            expected = "not a number"
            actual = self.calc.substract("str", 10)
            self.assertEqual(actual, expected)

    # pow test old
    def test_power_2_3(self):
        expected = 8
        actual = self.calc.power(2, 3)
        self.assertEqual(actual, expected)

    def test_power_negative_num(self):
        expected = -27
        actual = self.calc.power(-3, 3)
        self.assertEqual(actual, expected)

    def test_power_negative_sign(self):
        expected = 0.01
        actual = self.calc.power(3, -4)
        actual = round(actual, 2)
        self.assertEqual(actual, expected)

    def test_power_negative_sign_num(self):
        expected = -0.125
        actual = self.calc.power(-2, -3)
        actual = round(actual, 3)
        self.assertEqual(actual, expected)

    # pow test new
    def test_power_negative_int_negative_int(self):
        expected = -0.125
        actual = self.calc.power(-2, -3)
        self.assertEqual(actual, expected)

    def test_power_int_zero(self):
        expected = 1
        actual = self.calc.power(3, 0)
        self.assertEqual(actual, expected)

    def test_power_zero_zero(self):
        expected = 1
        actual = self.calc.power(0, 0)
        actual = round(actual, 2)
        self.assertEqual(actual, expected)

    def test_power_float_int(self):
        expected = 6.25
        actual = self.calc.power(2.5, 2)
        actual = round(actual, 3)
        self.assertEqual(actual, expected)

    # square root test old
    def test_square_positive(self):
        expected = 3
        actual = self.calc.square_root(9)
        self.assertEqual(expected, actual)

    def test_square_negative(self):
        with self.assertRaises(ValueError):
            expected = "Number can't be negative"
            actual = self.calc.square_root(-9)
            self.assertEqual(expected, actual)

    def test_square_float(self):
        expected = 3.08
        actual = self.calc.square_root(9.5)
        actual = round(actual, 2)
        self.assertEqual(expected, actual)

    def test_square_zero(self):
        expected = 0
        actual = self.calc.square_root(0)
        self.assertEqual(expected, actual)

    # square root test new
    def test_square_positive(self):
        expected = 5
        actual = self.calc.square_root(25)
        self.assertEqual(expected, actual)

    def test_square_negative(self):
        with self.assertRaises(ValueError):
            expected = "Number can't be negative"
            actual = self.calc.square_root(-81)
            self.assertEqual(expected, actual)

    def test_square_float(self):
        expected = 3.08
        actual = self.calc.square_root(9.5)
        actual = round(actual, 2)
        self.assertEqual(expected, actual)

    def test_square_zero(self):
        expected = 0
        actual = self.calc.square_root(0)
        self.assertEqual(expected, actual)

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
