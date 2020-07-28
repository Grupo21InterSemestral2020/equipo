from os import system,name
def limpiar_pantalla():
    if name=='nt':
        system('cls')
    else:
        system('clear')

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
                print("BIENVENIDO A MENU CURSO-TEMA-VIDEO")
                opcion=int(input("""
                ¿Qué Desea hacer?
                1)Agregar
                2)Borrar
                3)Modificar
                4)Consultar
                5)Elegir Clave
                6)Salir
                Opcion: """))
                if opcion<1:
                    limpiar_pantalla()
                    input("Error, introduzca numero correcto.")
                elif opcion==1:
                    limpiar_pantalla()
                    idctema=open("curso_temas_videos.txt","r",encoding='utf8')
                    print(idctema.read())
                    input("Base de datos Actual.")
                    idctema.close()
                    self.__IdCT=int(input("Dame el idCursoTema: "))
                    limpiar_pantalla()
                    videoid=open("videos.txt","r", encoding='utf8')
                    print(videoid.read())
                    input("Base de datos Actual.")
                    videoid.close()
                    self.__IdVideo=int(input("Dame el idvideo: "))
                    self.__IdCursoTV=self.__IdCursoTV+1
                    valores=Curso_tema_video(self.__IdCursoTV,self.__IdCT,self.__IdVideo)
                    lista.append(valores)
                    input("Registro Agregado")
                    limpiar_pantalla()
                elif opcion ==2:
                    limpiar_pantalla()
                    print(f"\n{'idCursoTV':<30}{'idCT':<30}{'idVideo':<30}")
                    for i1 in lista:
                        print(f"{i1.__IdCursoTV:<30}{i1.__IdCT:<30}{i1.__IdVideo:<30}")
                    if lista==[]:
                        input("Actualmente vacia.")
                        limpiar_pantalla()
                    else:
                        clave=int(input("Clave:"))
                        for remover in lista:
                            if remover.IdCursoTV == clave:
                                lista.remove(Curso_tema_video(clave,None,None))
                                input("Registro borrado.")
                                limpiar_pantalla()

                elif opcion ==3:
                    limpiar_pantalla()
                    print(f"\n{'idCursoTV':<30}{'idCT':<30}{'idVideo':<30}")
                    for i2 in lista:
                        print(f"{i2.__IdCursoTV:<30}{i2.__IdCT:<30}{i2.__IdVideo:<30}")
                    clave=int(input("Clave:"))
                    if lista==[]:
                        input("Registro vacio actualmente.")
                        limpiar_pantalla()
                    else:
                        for remover in lista:
                            if remover.IdCursoTV==clave:
                                remover.IdCT=int(input("Dame el Id curso nuevo: "))
                                remover.IdVideo=int(input("Dame el idvideo nuevo: "))
                                input("Registro Actualizado.")
                                limpiar_pantalla()

                elif opcion ==4:
                    limpiar_pantalla()
                    if lista==[]:
                        input("Registro vacio actualmente.")
                        limpiar_pantalla()
                    else:
                        print(f"\n{'idCursoTV':<30}{'idCT':<30}{'idVideo':<30}")
                        for i3 in lista:
                            print(f"{i3.__IdCursoTV:<30}{i3.__IdCT:<30}{i3.__IdVIdeo:<30}")
                        input("Presione enter para continuar.")
                        limpiar_pantalla()
                elif opcion ==5:
                    limpiar_pantalla()
                    print(f"\n{'idCursoTV':<30}{'idCT':<30}{'idVideo':<30}")
                    for i4 in lista:
                        print(f"{i4.__IdCursoTv:<30}{i4.__IdCT:<30}{i4.__IdVideo:<30}")
                    clave=int(input("Clave:"))
                    limpiar_pantalla()
                    print(f"\n{'idCursoTV':<30}{'idCT':<30}{'idVideo':<30}")
                    for i5 in lista:
                        if i5.icttv==clave:
                            print(f"{i5.__IdCursoTv:<30}{i5.__IdCT:<30}{i5.__IdVideo:<30}")
                    input("Enter para continuar.")

                elif opcion==6:
                    break
                elif opcion>6:
                    input("Error, introduzca numero correcto.")
                    limpiar_pantalla()
                def informacion():
                    archivo=open("curso_temas_videos.txt","w",encoding='utf8')
                    for i6 in lista:
                        archivo.write(str(f" IdCursoTV: {i6.__IdCursoTV}, IdCT: {i6.__IdCT}, IdVideo: {i6.__IdVideo}""\n"))
                    archivo.close()
                informacion()
                limpiar_pantalla()

            except ValueError:
                limpiar_pantalla()
                input("Error, introducir solo numeros, vuelva a intentar")


