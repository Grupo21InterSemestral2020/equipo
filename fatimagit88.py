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
        print(f"mouse: {self.__marca}, tipo: {self.__tipo}, color: {self.__color}")

mouse1 = Mouse("hp","dos botones","negro")
mouse2 = Mouse("dell","inalambrico","blanco")

#impresion llamando metodo
mouse1.imprimir()
mouse2.imprimir()

#impresion llamando objeto
print(f"mouse: {mouse1.marca}, tipo: {mouse1.tipo}, color: {mouse1.color}")
print(f"mouse: {mouse2.marca}, tipo: {mouse2.tipo}, color: {mouse2.color}")
    