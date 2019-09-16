import logging
import re

from collections import defaultdict
from typing import List, Set, Pattern, Tuple
from pprint import pprint


logging.getLogger().setLevel(logging.INFO)
SEPARATOR: str = 'ç'


def parse_data(dataset: Set) -> Tuple[int, int, dict]:
    # Slice object for check IDS
    ID: slice = slice(0, 3)

    data: List = list(dataset)
    sales: defaultdict = defaultdict(int)
    todos: defaultdict = defaultdict(int)
    number_of_sellers = number_of_customers = int()

    for row in data:
        line: List = row.split(SEPARATOR)
        sale_id = line[1]
        seller_name = line[3]
        print(line)

        # TODO: trocar para constantes que dão melhor significado
        if int(row[ID]) == 1:
            number_of_sellers += 1
        # TODO: trocar para constantes que dão melhor significado
        elif int(row[ID]) == 2:
            number_of_customers += 1
        else:
            sale_sum: float = get_sales_total_sum(line)
            todos.update({sale_id: sale_sum})
            # sales.update({sale_id: sale_sum})
            if sale_sum > sales[sale_id]:
                sales.update({sale_id: sale_sum})

            # print(seller_name, dict(todos))
            # worst_seller.update({seller_name: sale_sum})
    return (number_of_sellers, number_of_customers, sales)


def get_sales_total_sum(sales_list: List) -> float:
    SALE_REGEX: Pattern = re.compile(r'-(\d+)-([0-9]*\.?[0-9]*)[,]?')

    sale_sum: float = float()
    order_items = sales_list[2]

    for quantity, price in SALE_REGEX.findall(order_items):
        sale_sum += float(quantity) * float(price)

    return sale_sum
