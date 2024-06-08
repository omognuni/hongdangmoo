class OutOfStock(Exception):
    message = "Out of stock"

    def __str__(self):
        return self.message
