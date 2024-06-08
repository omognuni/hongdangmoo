from market.domain.entity import Product, Cart, CartLine


def add_to_cart(cart: Cart, line: CartLine):
    for idx, cart_line in enumerate(cart.cart_lines):
        if cart_line.product == line.product:
            cart_line.qty = line.qty
            return

    cart.cart_lines.append(line)


def remove_from_cart(cart: Cart, product: Product):
    delete_indexes = []
    for idx, cart_line in enumerate(cart.cart_lines):
        if cart_line.product == product:
            delete_indexes.append(idx)

    for idx in delete_indexes:
        del cart.cart_lines[idx]
