import unittest
import sys


class TestCore(unittest.TestCase):

    def test_minimum_python_version_required(self):
        CURRENT_PYTHON_VERSION: tuple = sys.version_info[:2]
        REQUIRED_PYTHON_VERSION: tuple = (3, 6)
        self.assertGreaterEqual(CURRENT_PYTHON_VERSION, REQUIRED_PYTHON_VERSION)
