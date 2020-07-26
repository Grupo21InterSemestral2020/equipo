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
            1.- Agregar tema.
            2.- Borrar tema.
            3.- Modificar tema.
            4.- Ver detalles del tema.
            5.- Consultar todo.
            6.- Salir.""")

            opc= int(input("Elija una opcion: "))
            if opc == 1:
                self.__idTema= self.__idTema+1
                self.__nombre=input("Nombre del tema: ")
                info= Tema(self.__idTema,self.__nombre)
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
                            tema.remove(Tema(id,None))
                            input("El registro fue borrado. ")

            elif opc == 3:
                id = int(input("ID: "))
                if tema == []:
                    print("No hay información.")
                else:
                    for remover in tema:
                        if remover.idTema == id:
                            remover.nombre = input ("Nombre nuevo del tema: ")
                            print("Registro actualizado.")

            elif opc == 4:
                id = int(input("ID: "))
                if tema == []:
                    input("No hay información.")
                else:
                    print(f"{'idTema': <20} {'Nombre' :<20}")

            elif opc == 5:
                if tema ==[]:
                    print("No hay informacion. ")
                else:
                    for element in tema:
                        print (element)
            
            elif opc == 6:
                print("Saliendo del programa. ")
                break

            else:
                print("""
                Error.
                Favor de introducir solo numeros de las opciones. """)


            def guardar():
                f = open("./archivos/temas.txt","w")
                for posicion in tema:
                    f.write(str(f" ID TEMA: {posicion.idTema}, NOMBRE: {posicion.nombre}"))
                    f.close()
            guardar()

