import unittest
import math

def square_root(x):
    if x < 0:
        raise ValueError("Not for a negative number")
    return math.sqrt(x)

class TestCalculator(unittest.TestCase):

    def test_square_root_positive_number(self):
        result = square_root(9)
        self.assertEqual(result, 3)

    def test_square_root_zero(self):
        result = square_root(0)
        self.assertEqual(result, 0)

    def test_square_root_negative_number(self):
        with self.assertRaises(ValueError):
            square_root(-9)

    def test_square_root_one(self):
        result = square_root(1)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
