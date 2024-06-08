from market.domain.entity import Product, Cart, CartLine


def add_to_cart(cart: Cart, product: Product, qty: int):
    for idx, cart_line in enumerate(cart.cart_lines):
        if cart_line.product == product:
            product.available_quantity += cart_line.qty - qty
            cart_line.qty = qty
            return
    product.available_quantity -= qty
    line = CartLine(product, qty)
    cart.cart_lines.append(line)


def remove_from_cart(cart: Cart, product: Product):
    delete_indexes = []
    for idx, cart_line in enumerate(cart.cart_lines):
        if cart_line.product == product:
            delete_indexes.append(idx)

    for idx in delete_indexes:
        product.available_quantity += cart.cart_lines[idx].qty
        del cart.cart_lines[idx]
