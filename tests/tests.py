import unittest
import os
import sys

from pathlib import Path

from source.directory import _create_dir
from source.parser import get_higher_sales_value, get_higher_sales_value_per_seller


class TestDirectory(unittest.TestCase):
    def setUp(self):
        self.home_path = Path.home()
        self.path_to_test = self.home_path / 'test'

    def tearDown(self):
        os.rmdir(self.path_to_test)

    def test_create_dir_in_home_path(self):
        _create_dir(self.path_to_test)
        self.assertTrue(self.path_to_test.exists())


class TestCore(unittest.TestCase):

    def test_minimum_python_version_required(self):
        CURRENT_PYTHON_VERSION: tuple = sys.version_info[:2]
        REQUIRED_PYTHON_VERSION: tuple = (3, 6)
        self.assertGreaterEqual(CURRENT_PYTHON_VERSION, REQUIRED_PYTHON_VERSION)


class TestParserHelpFunctions(unittest.TestCase):
    def test_higher_sales_value(self):
        list_test = ['0', '0', '[0-1-10]', '_']
        self.assertEqual(get_higher_sales_value(list_test), 10.0)

    def test_higher_sales_value_per_seller(self):
        list_test = [('x', '1', 10.10), ('x', '1', 1.00)]
        result = get_higher_sales_value_per_seller(list_test)
        self.assertEqual(result['x'], 11.1)
