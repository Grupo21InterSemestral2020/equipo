class Temas:
    def __init__(self,IdTemas,administracion,usuario):
        self.__IdTemas = IdTemas
        self.__administracion = administracion
        self.__usuario = usuario

    @property
    def IdTemas(self):
        return self.__IdTemas

    @IdCurso.setter
    def IdTemas(self,valor):
        self.__IdTemas = valor

    @property
    def administracion(self):
        return self.__administracion

    @administracion.setter
    def administracion(self,valor):
        self.__administracion = valor

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self,valor):
        self.__usuario = valor

    def imprimirInfo(self,IdTemas,administracion,usuario,f):
        f = open("./PIAequipo/Temas.txt","a",encoding="utf8")
        IdTemas = int(input("Ingrese un IdTemas: "))
        administracion = input("¿Que desea modificar?: ")
        usuario = input("Ingrese nombre del usuario: ")
        f.write(str(IdTemas) + "|" + (administracion) + "|" + (usuario) + "\n" )
        f.close()