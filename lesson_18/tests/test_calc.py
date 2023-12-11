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


if __name__ == '__main__':
    unittest.main()
