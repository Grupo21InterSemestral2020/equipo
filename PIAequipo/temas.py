class Tema:
    def __init__(self,idTema,nombre):
        self.__idTema = idTema
        self.__nombre = nombre

    @property
    def idTema(self):
        return self.__idTema

    @idTema.setter
    def id(self,idTema):
        self.__idTema = idTema 

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    def menu(self):
        tema = []
        while True:
            print(f"{'BIENVENIDO AL MENU DE TEMAS.': <20}")
            print ("""
            1.- Agregar tema
            2.- Borrar tema
            3.- Modificar tema
            4.- Ver detalles del tema
            5.- Salir""")

            opc= int(input("Elija una opcion: "))
            if opc == 1:
                self.__idTema= self.__idTema+1
                self.__nombre=input("Nombre del tema: ")
                info= Tema(self.__idTema,señf.__nombre)
                tema.append(info)
                print("Tema agregado.")
                break
            
            elif opc == 2:
                if tema == []:
                    print("No hay información.")
                else: 
                    id = int(input("ID del tema: "))
                    for remover in tema:
                        if remover.idTema == id:
                            tema.remove(Tema(clave,None))
                            input("El registro fue borrado. ")

            

valor = Tema(1,None)
valor.menu()
