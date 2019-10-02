import unittest
from source.parser import get_higher_sales_value, get_higher_sales_value_per_seller, accepted_file_extension


class TestParserHelpFunctions(unittest.TestCase):
    def test_higher_sales_value(self):
        list_test = ['0', '0', '[0-1-10]', '_']
        self.assertEqual(get_higher_sales_value(list_test), 10.0)

    def test_higher_sales_value_per_seller(self):
        list_test = [('x', '1', 10.10), ('x', '1', 1.00)]
        result = get_higher_sales_value_per_seller(list_test)
        self.assertEqual(result['x'], 11.1)

    def test_accepted_file_extension_checker(self):
        filename = 'this.dat'
        self.assertTrue(accepted_file_extension(filename))
