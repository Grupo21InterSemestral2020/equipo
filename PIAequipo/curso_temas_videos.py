class Curso_tema_video:
    def __init__(self,IdCursoTV,IdCT,IdVideo):
        self.__IdCursoTV = IdCursoTV
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

                elif opcion ==2:
                    print("")
                    print(f"\n{'idCursoTV':<30}{'idCT':<30}{'idVideo':<30}")
                    for i1 in lista:
                        print(f"{i1.icttv:<30}{i1.ict:<30}{i1.iv:<30}")
                    if lista==[]:
                        input("Actualmente vacia, enter para continuar...")
                        print("")
                    else:
                        clave=int(input("Clave:"))
                        for remover in lista:
                            if remover.icttv == clave:
                                lista.remove(Curso_Tema_Video(clave,None,None))
                                input("Registro borrado, enter para continuar...")
                                print("")


                elif opcion ==3:
                    print("")
                    print(f"\n{'idCursoTV':<30}{'idCT':<30}{'idVideo':<30}")
                    for i2 in lista:
                        print(f"{i2.icttv:<30}{i2.ict:<30}{i2.iv:<30}")
                    clave=int(input("Clave:"))
                    if lista==[]:
                        input("Registro vacio actualmente, enter para continuar...")
                        print("")
                    else:
                        for remover in lista:
                            if remover.icttv==clave:
                                remover.ict=int(input("Dame el idCT nuevo: "))
                                remover.iv=int(input("Dame el idvideo nuevo: "))
                                input("Registro Actualizado, enter para continuar...")
                            print("")

                elif opcion ==4:
                    print("")
                    if lista==[]:
                        input("Registro vacio actualmente, presione enter para continuar..")
                        print("")
                    lse:
                        print(f"\n{'idCursoTV':<30}{'idCT':<30}{'idVideo':<30}")
                        for i3 in lista:
                            print(f"{i3.icttv:<30}{i3.ict:<30}{i3.iv:<30}")
                        input("Presione enter para continuar...")
                        print("")



            except ValueError:
                    print(" ")
                    input("Error, introducir solo numeros, vuelva a intentar, enter para continuar...")


