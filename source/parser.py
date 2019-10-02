import re

from collections import defaultdict
from os import path
from typing import List, Set, Pattern, Tuple


SEPARATOR: str = 'ç'
SELLER_ID: int = 1
CUSTOMER_ID: int = 2
FILE_EXTENSION: str = '.dat'


def accepted_file_extension(string: str) -> bool:
    return path.splitext(string)[1] == FILE_EXTENSION


def parse_dat_file(dataset: Set) -> Tuple[int, int, dict, dict]:
    # Slice object for check IDS
    ID: slice = slice(0, 3)

    data, salesman_row = (list(dataset), list())
    sales: defaultdict = defaultdict(int)
    number_of_sellers = number_of_customers = int()

    for row in data:
        line: List = row.split(SEPARATOR)
        sale_id = line[1]
        seller_name = line[3]

        if int(row[ID]) == SELLER_ID:
            number_of_sellers += 1
        elif int(row[ID]) == CUSTOMER_ID:
            number_of_customers += 1
        else:
            sale_sum: float = get_higher_sales_value(line)
            salesman_row.append(tuple([seller_name, sale_id, sale_sum]))
            if sale_sum > sales[sale_id]:
                sales.update({sale_id: sale_sum})
    return (
        number_of_sellers,
        number_of_customers,
        sales,
        get_higher_sales_value_per_seller(salesman_row)
    )


def get_higher_sales_value(sales_list: List) -> float:
    """Function returns the sum of sell"""
    SALE_REGEX: Pattern = re.compile(r'-(\d+)-([0-9]*\.?[0-9]*)[,]?')
    ITEM_ROW: List = sales_list[2]
    sale_sum: float = float()
    for quantity, price in SALE_REGEX.findall(ITEM_ROW):
        sale_sum += float(quantity) * float(price)
    return sale_sum


def get_higher_sales_value_per_seller(data: List) -> dict:
    """Returns the sum of each seller's sale"""
    result: dict = dict()
    for name, _, value in data:
        total: float = result.get(name, 0) + value
        result[name] = total
    return result
