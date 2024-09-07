from importlib.metadata import files
from itertools import product
from pprint import pprint

class Product:
    def __init__(self, name:str, weihte:float, category:str):
        self.name = name
        self.weihte = weihte
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weihte}, {self.category}.'

class Shop:

    # __file_name = 'products.txt'

    def __init__(self):
        self.__file_name = 'products.txt'



     # def __init__(self, file):


    def get_products(self):
        file = open(self.__file_name, 'r')
        return file.read()
        file.close()

    def add(self,*products):
        list_products = self.get_products()
        for product in products:
            if product.name in list_products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{product}\n')
                file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)  # __str__
s1.add(p1, p2, p3)
print(s1.get_products())
