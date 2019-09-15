from collections import namedtuple

Seller = namedtuple('Seller', 'name cpf salary')
Customer = namedtuple('Customer', 'name cnpj BusinessArea')


class Order:
    def __init__(self, id: int, seller_name: str):
        self.id = id
        self.seller = seller_name


class OrderItem:
    def __init__(self):
        pass
