from market.domain.entity import Product, Cart, CartLine
from market.domain.exception import OutOfStock


def add_to_cart(cart: Cart, product: Product, qty: int):
    if product.available_quantity < qty:
        raise OutOfStock
    cart.add_product(product, qty)
    product.available_quantity -= qty


def remove_from_cart(cart: Cart, product: Product):
    for cart_line in cart.cart_lines:
        if cart_line.product == product:
            product.available_quantity += cart_line.qty
    cart.remove_product(product)
