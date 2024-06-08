from dataclasses import dataclass


class Product:

    def __init__(self, id: int, name: str, price: int, available_quantity: int):
        self.id = id
        self.name = name
        self.price = price
        self.available_quantity = available_quantity

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return other.id == self.id

    def __hash__(self):
        return hash(self.id)


class CartLine:

    def __init__(self, product: Product, qty: int):
        self.product = product
        self.qty = qty


class Cart:
    def __init__(self, cart_lines: list = []):
        self.cart_lines = cart_lines


class Order:
    pass
