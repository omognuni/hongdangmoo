from market.models import Product, Cart, CartLine


def add_to_cart(cart, product, qty):
    pass


def remove_from_cart(cart, product, qty):
    pass


def test_add_product_to_cart():
    product = Product(
        id="keyboard-001", name="Keyboard", price=1000, available_quantity=10
    )
    cart = Cart()

    add_to_cart(cart, product, qty=1)

    assert product.available_quantity == 9


def test_remove_from_cart():
    product = Product(
        id="keyboard-001", name="Keyboard", price=1000, available_quantity=9
    )
    line = CartLine(product=product, qty=2)
    cart = Cart(cart_lines=[line])

    remove_from_cart(cart, product, qty=1)

    assert product.available_quantity == 10
    assert cart.cart_lines[0].qty == 1
