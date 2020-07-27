from os import system,name
def limpiar_pantalla():
    if name == "nt":
        system("cls")
    else:
        system("clear")

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
        limpiar_pantalla()
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
            if opc < 1:
                limpiar_pantalla()
                input("Introduzca un numero del menu.")

            if opc == 1:
                limpiar_pantalla()
                self.__idTema= self.__idTema+1
                self.__nombre=input("Nombre del tema: ")
                info= Tema(self.__idTema,self.__nombre)
                tema.append(info)
                limpiar_pantalla()

            elif opc == 2:
                limpiar_pantalla()
                if tema == []:
                    input("No hay información.")
                    limpiar_pantalla()
                else: 
                    id = int(input("ID del tema: "))
                    for remover in tema:
                        if remover.idTema == id:
                            tema.remove(Tema(id,None))
                            input("El registro fue borrado. ")
                            limpiar_pantalla()

            elif opc == 3:
                limpiar_pantalla()
                id = int(input("ID: "))
                if tema == []:
                    print("No hay información.")
                    limpiar_pantalla()
                else:
                    for remover in tema:
                        if remover.idTema == id:
                            remover.nombre = input ("Nombre nuevo del tema: ")
                            print("Registro actualizado.")
                            limpiar_pantalla()

            elif opc == 4:
                limpiar_pantalla()
                id = int(input("ID: "))
                if tema == []:
                    input("No hay información.")
                    limpiar_pantalla()
                else:
                    print(f"{'idTema': <20} {'Nombre' :<20}")
                    limpiar_pantalla()

            elif opc == 5:
                limpiar_pantalla()
                if tema ==[]:
                    print("No hay informacion. ")
                    limpiar_pantalla()
                else:
                    for element in tema:
                        print (element)
                        limpiar_pantalla()
            
            elif opc == 6:
                print("Saliendo del programa. ")
                break

            else:
                print("""
                Error.
                Favor de introducir solo numeros de las opciones. """)
                limpiar_pantalla()


            def guardar():
                f = open("./archivos/temas.txt","w")
                for posicion in tema:
                    f.write(str(f" ID TEMA: {posicion.idTema}, NOMBRE: {posicion.nombre}"))
                    f.close()
            guardar()

