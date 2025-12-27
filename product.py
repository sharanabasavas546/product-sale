class Product:
    def __init__(self, pid, price):
        self.pid = pid
        self.price = price


class ProductManager:
    def __init__(self):
        self.products = {}

    def add(self, product):
        self.products[product.pid] = product

    def update(self, pid, price):
        if pid in self.products:
            self.products[pid].price = price
            return True
        return False
