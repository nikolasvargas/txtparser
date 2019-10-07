from dataclasses import dataclass
from source.identifier import Identifier


@dataclass
class Salesman(Identifier):
    name: str
    cpf: str
    salary: float
    IDENTIFIER: int = 1

    @classmethod
    def identifier(cls):
        return cls.IDENTIFIER


@dataclass
class Customer(Identifier):
    name: str
    cnpj: str
    business_area: str
    IDENTIFIER: int = 2

    @classmethod
    def identifier(cls):
        return cls.IDENTIFIER


@dataclass
class Item(Identifier):
    id: int
    price: float
    quantity: int
    IDENTIFIER: int = 3

    @classmethod
    def identifier(cls):
        return cls.IDENTIFIER
