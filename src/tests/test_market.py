from market.domain.entity import Product, Cart, CartLine
from market.domain.service import add_to_cart, remove_from_cart


def test_add_product_to_cart():
    product = Product(id=1, name="Keyboard", price=1000, available_quantity=10)
    cart = Cart()

    add_to_cart(cart, product, qty=1)

    assert product.available_quantity == 9


def test_remove_from_cart():
    product = Product(id=1, name="Keyboard", price=1000, available_quantity=9)
    cart = Cart()
    add_to_cart(cart, product, qty=2)

    remove_from_cart(cart, product)

    assert product.available_quantity == 9
    assert cart.cart_lines == []
