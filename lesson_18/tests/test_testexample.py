import sys
import unittest


class TestExample(unittest.TestCase):
    # def setUpClass(self):
    #     print('setUpClass')
    #     self.foo = 'foo'
    #
    # def tearDownClass(self):
    #     print('tearDownClass')
    #     del self.foo

    def setUp(self):
        print('setUp')
        self.expected_foo = 'foo'

    def tearDown(self):
        print('tearDown')
        del self.expected_foo

    @unittest.skip('Demonstrating skip mechanism')
    def test_lower(self):
        print('Test lower')
        self.assertEqual('foo', self.expected_foo)

    @unittest.skipUnless(sys.platform.startswith('linux'), 'Requires Ubuntu')
    def test_islower(self):
        print('Test islower')
        self.assertTrue('foo'.islower())

    @unittest.skipIf(sys.version_info[0] != 2, 'Requires Python version 2')
    def test_isdigit(self):
        print('Test isdigit')
        self.assertTrue('123'.isdigit())


if __name__ == '__main__':
    unittest.main()
