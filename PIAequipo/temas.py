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
            print(f"""
            BIENVENIDOS AL MENU DE TEMAS""")
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

            elif opc == 2:
                if tema == []:
                    input("No hay información.")
                else: 
                    clave = int(input("ID del tema a borrar: "))
                    for remover in tema:
                        if remover.__idTema == clave:
                            tema.remove(Tema(clave,None))
                            input("El registro fue borrado. ")

            elif opc == 3:
                clave = int(input("ID: "))
                if tema == []:
                    input("No hay información.")
                else:
                    for remover in tema:
                        if remover.idTema == clave:
                            remover.nombre = input ("Nombre nuevo del tema: ")
                            input("Registro actualizado.")

            elif opc == 4:
                clave = int(input("ID: "))
                if tema == []:
                    input("No hay información.")
                else:
                    input(f"{self.__idTema: <20}{self.__nombre :<20}")

            
            elif opc == 5:
                if tema ==[]:
                    input("Registro vacio actualmente")
                else:
                    print(f"{'idTema':<20}{'nombre':<20}")

                    for posicion in tema:
                        print(f"{posicion.idTema:<20}{posicion.nombre:<20}")
            
            elif opc == 6:
                break

            elif opc > 6:
                input("""Error. Favor de introducir solo numeros de las opciones. """)

            def guardar():
                archivo = open(".temas.txt","w", encoding='utf8')
                for posicion in tema:
                    archivo.write(str(f" idTema: {posicion.idTema}, nombre: {posicion.nombre}" "\n"))
                archivo.close()
            guardar()

