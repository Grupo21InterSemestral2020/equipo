class Mouse:
    def __init__(self,marca,color,tipo):
        self.__marca = marca
        self.__color = color
        self.__tipo = tipo 

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self,valor):
        self.__marca = valor
    
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self,valor):
        self.__color = valor

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self,valor):
        self.__tipo = valor 
    
    @classmethod
    def imprimirInfo(cls):
        print(f"la marca del mouse es: {self.__marca}, el color es: {self.__color}, y el tipo: {self.__tipo}")

mouse1 = Mouse("HP","negro","inalambrico")
mouse2 = Mouse("Microsoft","blanco","clasico")