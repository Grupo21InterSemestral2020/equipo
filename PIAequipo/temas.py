class Tema:
    def __init__(self,idTema,nombre):
        self.__idTema = idTema
        self.__nombre = nombre

    @property
    def idTema(self):
        return self.__idTema

    @idTema.setter
    def id(self,idTema):
        self.__idTema = idTema 

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    def opciones(self):
        temas = []
        while True:
            print ("""
            1.- Agregar tema
            2.- Borrar tema
            3.- Modificar tema
            4.- Ver detalles del tema
            5.- Salir""")

            opc= int(input("Elija una opcion: "))
            if opc == 1:
                f = open("./PIAequipo/temas.txt","a",encoding="utf8")
                self.__idTema= self.__idTema+1
                self.__nombre=input("Nombre del tema: ")
                f.write(str(self.__idTema) + "|" + self.__nombre + "\n")
                f.close()
            else:
                pass

