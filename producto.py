class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = max(0, stock)

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
    def stock(self, cantidad):
        self.__stock = max(0, cantidad)

    def __str__(self):
        return f"Producto: {self.__nombre}, Precio: ${self.__precio}, Stock: {self.__stock}"
