from file_parse import parse_csv
from product import Product
class Inventory:
    def __init__(self):
        self.products = []

    def __iter__(self):
        return self.products.__iter__()

    def __len__(self):
        return len(self.products)

    def __getitem__(self, index):
        return self.products[index]

    def __contains__(self, name):
        return any([p.name == name for p in self.products])

    def add_product(self, product):
        self.products.append(product)

    def total_cost(self):
        # return sum(p.cost() for p in self.products)
        return sum(p.cost for p in self.products) # modified p.cost with @property

    @classmethod
    def from_csv(cls, lines, **opts):
        # my_inv = Inventory()
        my_inv = cls() #creaing empty instance
        invdict =  parse_csv(lines, select=["name", "quant", "price"], types=[str, int, float], **opts)
        for p in invdict:
            pr = Product(**p)
            my_inv.add_product(pr)
        return my_inv