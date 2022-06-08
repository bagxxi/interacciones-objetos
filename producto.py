class Producto():
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock if stock > 0 else 0

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, stock):
        self.__stock = stock if stock > 0 else 0

    def __add__(self, other):
        return self.stock + other.stock

    def __sub__(self, other):
        return self.stock - other.stock

    def __eq__(self, other):
        return self.nombre == other.nombre