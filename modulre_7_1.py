from pprint import pprint

class Product:

    def __init__(self, name, weight=float, *category):
        self.name = str(name)
        self.weight = weight
        self.category = str(category)

    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.category}')


class Shop():

    def __init__(self, __file_name = 'products.txt'):
        self.__file_name = __file_name

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return str(products)

    def add(self, *products):

        for product in products:
            if str(product) not in self.get_products():
                file = open(self.__file_name, 'a')
                file.write(f' \n {str(product)}')
                file.close()
            else:
                print(f'Продукт {str(product)} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())