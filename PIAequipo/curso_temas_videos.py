class Curso_tema_video:
    def __init__(self,IdCursoTV,IdCT,IdVideo):
        self.__IdCursoTV = IdCusoTV
        self.__IdCT = IdCT
        self.__IdVideo = IdVideo

    @property
    def IdCursoTV(self):
        return self.__IdCursoTV

    @IdCursoTV.setter
    def IdCursoTV(self,valor):
        self.__IdCursoTV = valor

    @property
    def IdCT(self):
        return self.__IdCT

    @IdCT.setter
    def IdCT(self,valor):
        self.__IdCT = valor

    @property
    def IdVideo(self):
        return self.__IdVideo

    @IdVideo.setter
    def IdVideo(self,valor):
        self.__IdVideo = valor 

    def __eq__(self,otro):
        return self.__IdCursoTV == otro.__IdCursoTV
    def minimenu(self):
        limpiar_pantalla()
        lista = []

        while True:
            try:
                opcion=int(input("¿Qué Desea hacer?\n1)Agregar\n2)Borrar\n3)Modificar\n4)Consultar\n5)Elegir Clave\n6)Salir\nOpcion:"))
                if opcion<1:
                    print(" ")
                    input("Error, introduzca numero correcto, enter para continuar...")
                elif opcion==1:
                    print(" ")
                    idctema=open("./archivos/Curso_Tema.txt","r")
                    print(idctema.read())
                    input("Base de datos Actual, enter para continuar...")
                    idctema.close()
                    self.__ict=int(input("Dame el idCursoTema: "))
                    print(" ")
                    videoid=open("./archivos/VIDEO.txt","r")
                    print(videoid.read())
                    input("Base de datos Actual, enter para continuar...")
                    videoid.close()
                    self.__iv=int(input("Dame el idvideo: "))
                    self.__icttv=self.__icttv+1
                    valores=Curso_Tema_Video(self.__icttv,self.__ict,self.__iv)
                    lista.append(valores)
                    input("Registro Agregado, enter para continuar...")
                    print(" ")

            except ValueError:
                    print(" ")
                    input("Error, introducir solo numeros, vuelva a intentar, enter para continuar...")


