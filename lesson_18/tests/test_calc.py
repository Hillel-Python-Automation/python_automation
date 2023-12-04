import unittest
from ..app.calc import Calculator
from parameterized import parameterized


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        print(id(self.calc))

    def tearDown(self):
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


if __name__ == '__main__':
    unittest.main()
