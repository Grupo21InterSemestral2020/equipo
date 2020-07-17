class Mouse:

    def __init__(self,marca,color,tipo):
        self.__marca = marca
        self.__tipo = tipo
        self.__color = color

    @property
    def marca(self):
        return self.__marca

    @property
    def tipo(self):
        return self.__tipo

    @property
    def color(self):
        return self.__color

    @marca.setter
    def marca(self,nuevomarca):
        self.__marca = nuevomarca

    @tipo.setter
    def tipo(self,nuevotipo):
        self.__tipo= nuevotipo

    @color.setter
    def color(self,nuevocolor):
        self.__color = nuevocolor

    def imprimir(self):
        print(f"mouse: {self.marca}, tipo: {self.tipo}, color: {self.color}")

mouse1 = Mouse("hp","dos botones","negro")
mouse2 = Mouse("dell","inalambrico","blanco")

mouse1.imprimir
mouse2.imprimir