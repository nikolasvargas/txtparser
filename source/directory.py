import os
import logging
from pathlib import Path
from typing import Callable

logging.basicConfig(format='%(levelname)s: %(message)s')

INPUT_DIRECTORY: str = 'data/in'
OUTPUT_DIRECTORY: str = 'data/out'


def create_inpath() -> Callable:
    return _create_dir(INPUT_DIRECTORY)


def create_outpath() -> Callable:
    return _create_dir(OUTPUT_DIRECTORY)


def _create_dir(dir_name: str) -> (str, None):
    path: str = Path.home() / dir_name

    if path.exists():
        logging.error(f"Dir exists: {path}")
        logging.warning(f"Using existing path...")
        return False

    os.makedirs(path)


def create_file(filename: str, data: str):
    """
    Cria um arquivo {filename}.done.dat no OUTPUT_DIRECTORY definido
    Escreve no arquivo os dados que foram passados por argumenot
    """
    path: str = Path.home() / OUTPUT_DIRECTORY

    if path.exists():
        fullpath: str = f"{path}/{filename}.done.dat"

    create_outpath()
    fullpath: str = f"{path}/{filename}.done.dat"

    with open(fullpath, 'w') as new_file:
        new_file.write(str(data))
