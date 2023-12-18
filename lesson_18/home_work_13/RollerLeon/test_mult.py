import unittest

def mult(a, b):
    return a * b

class TestCalculator(unittest.TestCase):

    def test_mult_positive_numbers(self):
        result = mult(2, 2.5)
        self.assertEqual(result, 5)

    def test_mult_negative_numbers(self):
        result = mult(-2, 5)
        self.assertEqual(result, -10)

    def test_mult_zero(self):
        result = mult(7, 0)
        self.assertEqual(result, 0)

    def test_mult_two_negative_numbers(self):
        result = mult(-3, -2)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
