class Mouse:
    def __init__(self,marca,color,tipo):
        self.__marca = marca
        self.__color = color
        self.__tipo = tipo

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self,otraMarca):
        self.__marca = otraMarca

     @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self,nuevocolor):
        self.__color = nuevocolor
    
     @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self,otroTipo):
        self.__tipo = otroTipo

    def informacion(self):
        print(f'Marca:{self.__marca}, Color:{self.__color}, Tipo:{self.__tipo}')
        