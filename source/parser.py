#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging
import re

from glob import glob
from os.path import splitext
from pathlib import Path
from typing import BinaryIO, List, Set, AnyStr

from directory import INPUT_DIRECTORY
from models import Seller, Customer, Order, OrderItem


INPUT_PATH: str = Path.home() / INPUT_DIRECTORY
SEPARATOR: str = 'ç'
FILE_EXTENSION: str = '.dat'

logging.getLogger().setLevel(logging.INFO)


def search_batch_files() -> List:
    logging.info(f"loading all .dat files in {INPUT_PATH}")
    return glob(f"{INPUT_PATH}/*{FILE_EXTENSION}")


def read_large_file(file_object: BinaryIO):
    """
    Generator to read a large file(lazily)
    """
    while True:
        data: AnyStr = file_object.readline()
        if not data:
            break
        yield data


def process_file() -> None:
    for pathfile in search_batch_files():
        dataset: Set = set()
        try:
            with open(pathfile) as file_handler:
                for line in read_large_file(file_handler):
                    dataset.update(r for r in line.splitlines())
        except (IOError, OSError) as e:
            logging.ERROR(f"Something is wrong: {e}")

        parse_data(dataset)


def process_all_files() -> Set:
    rows: Set = set()
    for pathfile in search_batch_files():
        try:
            with open(pathfile) as file_handler:
                for line in read_large_file(file_handler):
                    rows.update(r for r in line.splitlines())
        except (IOError, OSError) as e:
            logging.ERROR(f"Something is wrong: {e}")
    return rows


def parse_data(dataset: Set):
    # Slice object for check IDS
    ID: slice = slice(0, 3)

    # Sale regex
    OLD_REGEX = re.compile(r'-(\d+)-([0-9]*\.?[0-9]*)[,]?')
    SALE_REGEX = re.compile(r'([0-9][,]?)-(\d+)-([0-9]*\.?[0-9]*)[,]?')

    CPF = CPNJ = 1
    SELLER_NAME = CUSTOMER_NAME = ORDER_ITEMS = 2
    SALARY = BUSINESS_AREA = SALES_MAN = 3

    data: List = list(dataset)
    number_of_sellers = number_of_customers = most_expensive_sale_id = worst_seller_id = int()

    for row in data:
        line = row.split(SEPARATOR)
        if int(row[ID]) == Seller.get_code():
            print(line)
            number_of_sellers += 1
        elif int(row[ID]) == Customer.get_code():
            number_of_customers += 1
        else:
            print(line)

            sale_id, sale_sum = (int(), float())
            for line_id, quantity, price in SALE_REGEX.findall(line[ORDER_ITEMS]):
                sale_id = line_id
                sale_sum += float(quantity) * float(price)


if __name__ == "__main__":
    data: List = list(process_all_files())
    process_file()
