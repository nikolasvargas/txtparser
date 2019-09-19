import os
import logging
from pathlib import Path
from shutil import copy2
from typing import Callable, Optional

logging.basicConfig(format='%(levelname)s: %(message)s')

INPUT_DIRECTORY: str = 'data/in'
OUTPUT_DIRECTORY: str = 'data/out'


def _copy_example_file():
    path: str = Path.home() / INPUT_DIRECTORY
    copy2('example.dat', path)


def create_inpath():
    _copy_example_file()
    _create_dir(INPUT_DIRECTORY)


def create_outpath() -> Callable:
    return _create_dir(OUTPUT_DIRECTORY)


def _create_dir(dir_name: str) -> Optional[bool]:
    path: str = Path.home() / dir_name

    if path.exists():
        logging.error(f"Dir exists: {path}")
        logging.warning(f"Using existing path...")
        return False

    os.makedirs(path)
