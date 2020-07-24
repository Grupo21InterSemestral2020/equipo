def limpiar_pantalla():
    if name == "nt":
        system("cls")
    else:
        system("clear")

class Cursos:
    def __init__(self,IdCurso,descripcion,IdEmpleado):
        self.__IdCurso = IdCurso
        self.__descripcion = descripcion
        self.__IdEmpleado = IdEmpleado

    @property
    def IdCurso(self):
        return self.__IdCurso

    @IdCurso.setter
    def IdCurso(self,valor):
        self.__IdCurso = valor

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self,valor):
        self.__descripcion = valor

    @property
    def IdEmpleado(self):
        return self.__IdEmpleado

    @IdEmpleado.setter
    def IdEmpleado(self,valor):
        self.__IdEmpleado = valor

    def __eq__(self,codigo):
       return self.__IdEmpleado = codigo

    def minimenu(self):
        limpiar_pantalla()
        lista =[]

        while true:
            try:


    def imprimirInfo(self,IdCurso,administracion,usuario,f):
        
        



        


    
