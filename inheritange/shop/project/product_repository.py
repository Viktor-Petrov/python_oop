from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for pr in self.products:
            if pr.name == product_name:
                return pr

    def remove(self, product_name):
        for pr in self.products:
            if pr.name == product_name:
                self.products.remove(pr)

    def __repr__(self):
        return '\n'.join([f"{p.name}: {p.quantity}" for p in self.products])


