import unittest

def division(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class TestCalculator(unittest.TestCase):

    def test_division_positive_numbers(self):
        result = division(6, 2)
        self.assertEqual(result, 3)

    def test_division_negative_numbers(self):
        result = division(-5, 2)
        self.assertEqual(result, -2.5)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            division(9, 0)

    def test_division_two_negative_numbers(self):
        result = division(-3, -2)
        self.assertEqual(result, 1.5)

if __name__ == '__main__':
    unittest.main()
