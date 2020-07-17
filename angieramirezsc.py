class Mouse:
    def __init__(self,marca,color,tipo):
        self.__marca = marca
        self.__color = color
        self.__tipo = tipo
    
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self,nuevaMarca):
        self.__marca = nuevaMarca
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self,nuevoColor):
        self.__color = nuevoColor

    @property
    def tipo(self):
        return self.__tipo
        
    @tipo.setter
    def tipo(self,nuevoTipo):
        self.__tipo = nuevoTipo
    