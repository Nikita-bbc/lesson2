class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products2.txt'
    def __init__(self):
        self.f = open(self.__file_name, 'r')
        self.existing_products = set(self.f.read().splitlines())
    def get_products(self):
        a = self.f.read()
        self.f.close()
        return a

    def add(self, *products):
        for item in products:
            if isinstance(item, Product):
                prod_str = str(item)
                if prod_str not in self.existing_products:
                    with open(self.__file_name, 'a') as f:
                        f.write(f'{prod_str}\n')
                    self.existing_products.add(prod_str)
                else:
                    print(f'Продукт {prod_str} уже есть в магазине')


p1 = Product('Potato', 54.4, 'Grocceries')
p2 = Product('Potato', 53.5, 'Daily')
p3 = Product('Potato', 54.4, 'POP')
s1 = Shop()
s1.add(p1, p2, p3)
print(s1.get_products())


