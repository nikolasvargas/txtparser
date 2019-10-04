from dataclasses import dataclass


@dataclass
class Salesman:
    name: str
    cpf: str
    salary: float

    @classmethod
    def foo(self):
        return 'foo'


@dataclass
class Customer:
    name: str
    cnpj: str
    business_area: str

    @classmethod
    def bar(cls):
        return 'bar'


@dataclass
class Item:
    id: int
    price: float
    quantity: int
