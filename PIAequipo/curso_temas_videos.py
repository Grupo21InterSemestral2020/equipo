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
        lista = []

        while True:
            try:
                opcion=int(input("""¿Qué Desea hacer?
                1)Agregar
                2)Borrar
                3)Modificar
                4)Consultar
                5)Elegir Clave
                6)Salir
                Opcion: """))
                if opcion<1:
                    input("Error, introduzca numero correcto.")
                elif opcion==1:
                    idctema=open("./archivos/curso_temas_videos.txt","r",encoding='utf8')
                    print(idctema.read())
                    input("Base de datos Actual.")
                    idctema.close()
                    self.__IdCT=int(input("Dame el idCursoTema: "))
                    videoid=open("./archivos/VIDEO.txt","r", encoding='utf8')
                    print(videoid.read())
                    input("Base de datos Actual.")
                    videoid.close()
                    self.__IdVideo=int(input("Dame el idvideo: "))
                    self.__IdCursoTV=self.__IdCursoTV+1
                    valores=Curso_tema_video(self.__IdCursoTV,self.__IdCT,self.__IdVideo)
                    lista.append(valores)
                    input("Registro Agregado")
                elif opcion ==2:
                    print(f"\n{'idCursoTV':<30}{'idCT':<30}{'idVideo':<30}")
                    for i1 in lista:
                        print(f"{i1.__idCursoTV:<30}{i1.IdCT:<30}{i1.IdVideo:<30}")
                    if lista==[]:
                        input("Actualmente vacia.")
                    else:
                        clave=int(input("Clave:"))
                        for remover in lista:
                            if remover.IdCursoTV == clave:
                                lista.remove(Curso_tema_video(clave,None,None))
                                input("Registro borrado.")


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
                    else:
                        print(f"\n{'idCursoTV':<30}{'idCT':<30}{'idVideo':<30}")
                        for i3 in lista:
                            print(f"{i3.icttv:<30}{i3.ict:<30}{i3.iv:<30}")
                        input("Presione enter para continuar...")
                        print("")

                elif opcion ==5:
                    print("")
                    print(f"\n{'idCursoTV':<30}{'idCT':<30}{'idVideo':<30}")
                    for i4 in lista:
                        print(f"{i4.icttv:<30}{i4.ict:<30}{i4.iv:<30}")
                    clave=int(input("Clave:"))
                    print("")
                    print(f"\n{'idCursoTV':<30}{'idCT':<30}{'idVideo':<30}")
                    for i5 in lista:
                        if i5.icttv==clave:
                            print(f"{i5.icttv:<30}{i5.ict:<30}{i5.iv:<30}")
                    input("Enter para continuar...")

                elif opcion==6:
                    break
                elif opcion>6:
                    input("Error, introduzca numero correcto, enter para continuar...")
                    print("")
                def informacion():
                    archivo=open("./archivos/Curso_Tema_Video.txt","w")
                    for i6 in lista:
                        archivo.write(str(f" IdCursoTV: {i6.icttv}, IdCT: {i6.ict}, IdVideo: {i6.iv}""\n"))
                    archivo.close()
                informacion()
                print("")


            except ValueError:
                    print(" ")
                    input("Error, introducir solo numeros, vuelva a intentar, enter para continuar...")


