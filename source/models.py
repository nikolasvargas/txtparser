class Seller:
    _CODE: int = 1
    _sellers: int = 0

    def __init__(self, name: str, cpf: int, salary: float):
        self.name = name
        self.cpf = cpf
        self.salary = salary
        Seller._sellers += 1

    @classmethod
    def get_sellers(cls) -> int:
        return cls._sellers

    @classmethod
    def get_code(cls) -> int:
        return cls._CODE


class Customer:
    _CODE = 2
    _customers: int = 0

    def __init__(self, name: str, cnpj: int, business_area: str):
        self.name = name
        self.cnpj = cnpj
        self.business_area = business_area
        Customer._customers = 1

    @classmethod
    def get_customers(cls):
        return cls._customers

    @classmethod
    def get_code(cls) -> int:
        return cls._CODE


class Order:
    _CODE = 3

    def __init__(self, id: int, salesman_name: str):
        self.id: int = id
        self.salesman_name: int = salesman_name

    def __repr__(self) -> str:
        fmt = "{}(id={}, salesman_name={!r})"
        return fmt.format(
            self.__class__.__name__,
            self.id,
            self.salesman_name
        )

    @classmethod
    def get_code(cls) -> int:
        return cls._CODE


class OrderItem:
    def __init__(self, id: int, quantity: int, price: float):
        self.id: int = id
        self.quantity: int = quantity
        self.price: float = price

    def __repr__(self) -> str:
        fmt: str = "{}(id={}, quantity={}, price={})"
        return fmt.format(
            self.__class__.__name__,
            self.id,
            self.quantity,
            self.price
        )
