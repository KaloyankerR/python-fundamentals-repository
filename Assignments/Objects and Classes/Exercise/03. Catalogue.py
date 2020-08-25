class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        return [x for x in self.products if x[0] == first_letter]

    def __repr__(self):
        sorted_products = [x for x in sorted(self.products)]
        result = f'Items in the {self.name} catalogue:\n'
        result += '\n'.join(sorted_products)
        return result
