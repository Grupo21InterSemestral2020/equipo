class Mouse:
    def _init_(self,marca,color,tipo):
        self.__marca = marca
        self.__color = color
        self.__tipo = tipo

@property
def marca(self):
    return self.__marca

@property
def color(self):
    return self.__color

@property
def tipo(self):
    return self.__tipo

@marca.setter
def marca(self.valor):
    return self.__marca= NuevaMarca

@color.setter
def color(self.color):
    return self.__color= NuevoColor

@tipo.setter
def tipo(self.tipo):
    return self.__tipo= NuevoTipo

def imprimirInfo(self):
        print(f"la marca del mouse es: {self.__marca}, el color es: {self.__color}, y el tipo: {self.__tipo}")

Mouse1 = Mouse("HP","negro","inalambrico")
Mouse2 = Mouse("Microsoft","blanco","clasico")

Mouse1.imprimirInfo()
Mouse2.imprimirInfo()