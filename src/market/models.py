from dataclasses import dataclass


class Product:

    def __init__(self, id: str, name: str, price: int, available_quantity: int):
        self.id = id
        self.name = name
        self.price = price
        self.available_quantity = available_quantity

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return other.id == self.id


@dataclass(frozen=True)
class CartLine:
    product: Product
    qty: int


class Cart:
    def __init__(self, cart_lines):
        self.cart_lines = cart_lines


class Order:
    pass
