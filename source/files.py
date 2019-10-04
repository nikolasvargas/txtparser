import logging

from glob import glob
from pathlib import Path
from typing import BinaryIO, List, Set, AnyStr, Optional

from directory import INPUT_DIRECTORY, OUTPUT_DIRECTORY
from parser import parse_dat_file, accepted_file_extension, FILE_EXTENSION


OUTPUT_PATH: str = Path.home() / OUTPUT_DIRECTORY
INPUT_PATH: str = Path.home() / INPUT_DIRECTORY

logging.getLogger().setLevel(logging.INFO)


def search_batch_files(filename_list: Optional[List[str]] = []) -> List[str]:
    """Return list with *.dat files found"""
    # we just want .dat(FILE_EXTENSION) files
    files: List = filter(accepted_file_extension, [f for f in filename_list])
    return [f for f in files] or glob(f"{INPUT_PATH}/*{FILE_EXTENSION}")


def read_large_file(file_object: BinaryIO):
    """
    Generator to read large files(lazily)
    """
    while True:
        data: AnyStr = file_object.readline()
        if not data:
            break
        yield data


def process_file(files: Optional[List[str]] = []):
    filename: str = str()
    for pathfile in search_batch_files(files):
        dataset: Set = set()
        try:
            with open(pathfile) as file_handler:
                filename = Path(file_handler.name).stem
                for line in read_large_file(file_handler):
                    dataset.update(r for r in line.splitlines())
                create_file(filename, parse_dat_file(dataset))
        except (IOError, OSError) as e:
            logging.ERROR(f"Something is wrong: {e}")


def create_file(filename: str, data: tuple):
    """
    Create file {filename}.done.dat in OUTPUT_PATH path
    Data received by argument is written to file
    """
    if not OUTPUT_PATH.exists():
        err_msg: str = f"Path {OUTPUT_PATH} does not exist"
        logging.ERROR(err_msg)

    fullpath: str = f"{OUTPUT_PATH}/{filename}.done.dat"
    (number_of_sellers, number_of_customers, sales, salesman) = data
    most_expensive_sale: int = sorted(sales.items(), key=lambda i: i[1])[-1][0]
    worst_salesman: str = sorted(salesman.items(), key=lambda i: i[1])[0]
    (salesman, value) = worst_salesman

    template: str = f"""
    Customer in input file: {number_of_sellers}
    Sellers in input file: {number_of_customers}
    Most expensive sale ID: {most_expensive_sale}
    Worst salesman: {salesman} (value: {value})
    """

    with open(fullpath, 'w') as new_file:
        logging.info(f"creating {fullpath}...")
        new_file.write(str(template))
        logging.info("Done")
