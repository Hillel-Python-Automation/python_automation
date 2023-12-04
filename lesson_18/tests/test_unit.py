import unittest


class TestSomething(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    @unittest.expectedFailure
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('FOO'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)


class TestAnotherSomething(unittest.TestCase):
    def test_isdigit(self):
        self.assertTrue('1234'.isdigit())


if __name__ == '__main__':
    unittest.main()
