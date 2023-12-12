import unittest
from lesson_18.app.calc import Calculator
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

    # До існуючих тестів дописати по 4 тести на кожну з непокритих тестами функцію:
    print("До існуючих тестів дописати по 4 тести на кожну з непокритих тестами функцію:")

    print('MULTIPLY')

    @parameterized.expand([
        ('\n''Two multiply two equals 4', 2, 2, 4),
        ('\n''Minus Two multiply two equals -4', -2, 2, -4),
        ('\n''Minus Three multiply Minus Three equals 9', -3, -3, 9),
        ('\n''Minus Seven multiply Three equals -21', -7, 3, -21)
    ])
    def test_multiply(self, _, a, b, expected_result):
        self.assertEqual(self.calc.mult(a, b), expected_result)

    def test_multiply2(self):
        self.assertEqual(self.calc.mult(3, 4), 12)

    print('DIVIDE')

    @parameterized.expand([
        ('\n''Four divide by Two equals 2', 4, 2, 2),
        ('\n''Minus Eight divide by Two equals -4', -8, 2, -4),
        ('\n''Minus Nine divided by  Minus Three equals 9', -9, -3, 3),
        ('\n''Minus Twenty one divide Three equals -7', -21, 3, -7)
    ])
    def test_division(self, _, a, b, expected_result):
        self.assertEqual(self.calc.div(a, b), expected_result)

    def test_division2(self):
        self.assertEqual(self.calc.div(3, 1), 3)

    print('SUBTRACT')

    def test_subtract(self):
        self.assertEqual(self.calc.substract(7, 4), 3)

    @parameterized.expand([
        ('Seven subtract Five equal Two', 7, 5, 2),
        ('Eleven subtract Six equal Five', 11, 6, 5),
        ('Ninty Nine subtract Two Hundred equal -101', 99, 200, -101)
    ])
    def test_subtract2(self, _, a, b, add_expected_result):
        self.assertEqual(self.calc.substract(a, b), add_expected_result)

    def test_subtract3(self):
        self.assertEqual(self.calc.substract(100, 101), -1)

    print('POWER')

    def test_pow(self):
        self.assertEqual(self.calc.power(2, 3), 8)

    @parameterized.expand([
        ('3 pow 3 equal 27', 3, 3, 27),
        ('4 pow 4 equal 256', 4, 4, 256)
    ])
    def test_pow2(self, _, a, b, expected_result):
        self.assertEqual(self.calc.power(a, b), expected_result)

    def test_pow3(self):
        self.assertEqual(self.calc.power(2, 3), 8)

    print('SQUARE ROOT')

    def test_sq_root(self):
        self.assertAlmostEqual(self.calc.square_root(2), 1.4142135623730951)

    def test_square_root_of_4(self):
        result = self.calc.square_root(4)
        self.assertEqual(result, 2.0)

    def test_square_root_of_100(self):
        result = self.calc.square_root(100)
        self.assertEqual(result, 10.0)

    def test_square_root_of_negative_number(self):
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)


if __name__ == '__main__':
    unittest.main()
