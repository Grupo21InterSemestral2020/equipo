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

    @administracion.sette
    def administracion(self,valor):
        self.__administracion = valor

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self,valor):
        self.__usuario = valor

    def imprimirInfo(self):
        print(f"Id: {self.__IdCurso}")
        print(f"administracion: {self.__administracion}")
        print(f"usuario: {self.__usuario}")
        


    
