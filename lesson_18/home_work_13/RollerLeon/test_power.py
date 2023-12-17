import unittest

def power(base, exponent):
    return base ** exponent

class TestCalculator(unittest.TestCase):

    def test_power_positive_numbers(self):
        result = power(3, 3)
        self.assertEqual(result, 27)

    def test_power_negative_exponent(self):
        result = power(4, -2)
        self.assertEqual(result, 0.0625)

    def test_power_zero_exponent(self):
        result = power(4, 0)
        self.assertEqual(result, 1)

    def test_power_base_zero_exponent(self):
        result = power(0, 2)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
