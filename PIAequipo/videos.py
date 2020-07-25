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

        def Minimenu(self):
            lista=[]
            while True:
                try:
                    opcion=int(input('''
                    Elige una opcion
                    1)Agregarvideo
                    2)Eliminarvideo
                    3)Modificarvideo
                    4)Vervideos
                    5)Elegir Id
                    6)Salir
                    >>Opcion:"))'''

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

                            if lista==[]
                            print("Esta vacia...")

                            else:
                                clave == int(input("clave: "))
                                for remover in lista:
                                    if remover.idV == clave:
                                        lista.remove(video(clave,None,None,None))
                                        print("Regirstro eliminado...")

                    elif opcion==3:
                        
                            


                        