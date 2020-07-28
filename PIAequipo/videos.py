from os import system,name
def limpiar_pantalla():
    if name=='nt':
        system('cls')
    else:
        system('clear')

class Video:
    def __init__ (self,idVideo,nombre,url,fecha):
        self.__idV = idVideo
        self.__nom = nombre
        self.__url = url
        self.__fechap = fecha

    @property
    def idV(self):
        return self.__idV

    @property
    def url(self):
        return self.__url
        
    @url.setter
    def url(self,valor):
        self.__url=valor

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self,valor):
        self.__nom=valor

    @property
    def fechap(self):
        return self.__fechap

    @fechap.setter
    def fechap(self,valor):
        self.__fechap = valor
    def __eq__ (self,otro):
        return self.__idV==otro.__idV

    def Minimenu(self):
        lista=[]
        while True:
            try:
                opcion=int(input('''
                BIENVENIDO AL MENU DE VIDEO
                Elige una opcion
                1)Agregarvideo
                2)Eliminarvideo
                3)Modificarvideo
                4)Vervideos
                5)Elegir Id
                6)Salir
                >>Opcion: '''))

                if opcion==1:
                    self.__idV=self.__idV+1
                    self.__nom= input("Asigna el nombre del video: ")
                    self.__url=int(input("Ingresa la url del video: "))
                    self.__fechap=int(input("Ingresa la fecha del video: "))

                    datos=Video(self.__idV,self.__nom,self.__url,self.__fechap)
                    lista.append(datos)
                    print("Se ha agregado el registro")

                elif opcion==2:
                    print(f"\n{'idVideo':<30}{'nombre':<30}{'url':<30}{'fecha':<30}")
                    for i1 in lista:
                        print(f"{i1.idV:<30}{i1.nom:<30}{i1.url:<30}{i1.fechap:<30}")
                    if lista==[]:
                        input("Esta vacia, enter para continuar...")
                    else:
                        clave=int(input("Introduce clave:"))
                        for remover in lista:
                            if remover.idV == clave:
                                lista.remove(Video(clave,None,None,None))
                            input("Registro eliminado, enter para continuar...")

                elif opcion==3:
                    print(f"\n{'idVideo':<30}{'nombre':<30}{'url':<30}{'fecha':<30}")
                    for i2 in lista:
                        print(f"{i2.idV:<30}{i2.nom:<30}{i2.url:<30}{i2.fechap:<30}")
                    clave=int(input("Clave:"))
                    if lista==[]:
                        input("Este registro esta vacio actualmente, enter para continuar...")
                    else:
                        for remover in lista:
                            if remover.idV==clave:
                                remover.nom=("Ingresa un nombre nuevo: ")
                                remover.url=int(input("Ingresa una url nueva: "))
                                remover.fechap=int(input("Ingresa una fecha nueva: "))
                            input("El registro actualizado, enter para continuar...")
 
                elif opcion==4:
                    limpiar_pantalla()
                    if lista==[]:
                        input("Registro vacio actualmente, enter para continuar...")
                        limpiar_pantalla()
                    else:
                        print(f"\n{'idVideo':<30}{'nombre':<30}{'url':<30}{'fecha':<30}")
                        for i3 in lista:
                            print(f"{i3.idV:<30}{i3.nom:<30}{i3.url:<30}{i3.fechap:<30}")
                        input("Presione enter para continuar...")
                        limpiar_pantalla()

                elif opcion==5:
                    limpiar_pantalla()
                    print(f"\n{'idVideo':<30}{'nombre':<30}{'url':<30}{'fecha':<30}")
                    for i4 in lista:
                        print(f"{i4.idV:<30}{i4.nom:<30}{i4.url:<30}{i4.fechap:<30}")
                    clave=int(input("Clave:"))
                    limpiar_pantalla()
                    print(f"\n{'idVideo':<30}{'nombre':<30}{'url':<30}{'fecha':<30}")
                    for i5 in lista:
                        if i5.icttv==clave:
                            print(f"{i5.idV:<30}{i5.nom:<30}{i5.url:<30}{i5.fechap:<30}")
                    input("Presiona enter para continuar...")
                elif opcion==6:
                    break
                else:
                    input("Introduce un numero valido")
                    limpiar_pantalla()

                def informacion():
                    archivo=open(".videos.txt","w")
                    for i6 in lista:
                        archivo.write(str(f" idVideo: {i6.idV}, nombre: {i6.nom}, url: {i6.url}, fecha: {i6.fechap}""\n"))
                    archivo.close()
                informacion()
                limpiar_pantalla()
            
            except ValueError:
                input("Se produjo un error, vuelve a intentar")