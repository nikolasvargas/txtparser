import unittest
import os
import sys

from pathlib import Path
from source.directory import _create_dir


class TestDirectory(unittest.TestCase):
    def setUp(self):
        self.home_path = Path.home()
        self.path_to_test = self.home_path / '01test01'

    def tearDown(self):
        os.rmdir(self.path_to_test)

    def test_create_dir_in_home_path(self):
        _create_dir(self.path_to_test)
        self.assertTrue(self.path_to_test.exists())
