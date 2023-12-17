import unittest

def subtract(a, b):
    return a - b

class TestCalculator(unittest.TestCase):

    def test_subtract_positive_numbers(self):
        result = subtract(8, 3)
        self.assertEqual(result, 5)

    def test_subtract_two_negative_numbers(self):
        result = subtract(-6, -3)
        self.assertEqual(result, -3)

    def test_subtract_mixed_numbers(self):
        result = subtract(5, -2)
        self.assertEqual(result, 7)

    def test_subtract_number_and_null(self):
        result = subtract(5, 0)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
