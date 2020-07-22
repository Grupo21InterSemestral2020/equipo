class Cursos:
    def __init__(self,IdCurso,administracion,usuario):
        self.__IdCurso = IdCurso
        self.__administracion = administracion
        self.__usuario = usuario

    @property
    def IdCurso(self):
        return self.__IdCurso

    @IdCurso.setter
    def IdCurso(self,valor):
        self.__IdCurso = valor

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

    def imprimirInfo(self,IdCurso,administracion,usuario,f):
        f = open("./PIAequipo/cursos.txt","a",encoding="utf8")
        IdCurso = int(input("Ingrese un IdCurso: "))
        administracion = input("¿Que desea modificar?: ")
        usuario = input("Ingrese nombre del usuario: ")
        f.write(str(IdCurso) + "|" + (administracion) + "|" + (usuario) + "\n" )
        f.close()
        



        


    
