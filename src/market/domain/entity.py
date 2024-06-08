from dataclasses import dataclass
from typing import List


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

    def update_quantity(self, qty: int):
        self.product.available_quantity += self.qty - qty
        self.qty = qty


class Cart:
    def __init__(self):
        self.cart_lines: List[CartLine] = []

    def add_product(self, product: Product, qty: int):
        for cart_line in self.cart_lines:
            if cart_line.product == product:
                cart_line.update_quantity(qty)
                return
        self.cart_lines.append(CartLine(product, qty))

    def remove_product(self, product: Product):
        self.cart_lines = [line for line in self.cart_lines if line.product != product]


class Order:
    pass
