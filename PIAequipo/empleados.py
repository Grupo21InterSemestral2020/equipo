class Empleado():
    def __init__(self,idEmpleado,nombre,direccion):
        self.__idEmpleado = idEmpleado
        self.__nombre = nombre
        self.__direccion = direccion

    @property
    def idEmpleado(self):
        return self.__idEmpleado

    @idEmpleado.setter
    def id(self,idEmpleado):
        self.__idEmpleado = idEmpleado 

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self,direccion):
        self.__direccion = direccion
    

    def menu(self):

        empleados = []
        while True:
            print(f"{'BIENVENIDO AL MENU EMPLEADOS':^20}")
            print ("""
            1. Agregar empleado
            2. Borrar empleado
            3. Modificar empleado
            4. Consultar todo. 
            5. Ver detalles de empleado
            6. Salir""")

            opcion= int(input("Elija una opcion: "))
            if opcion ==1:
                self.__idEmpleado= self.__idEmpleado+1
                self.__nombre=input("Ingresa el nombre del empleado: ")
                self.__direccion=input("Ingresa la direccion del empleado")
                info = Empleado(self.__idEmpleado,self.__nombre,self.__direccion)
                empleados.append(info)
                print("Empleado agregado.")

            elif opcion ==2:
                if empleados==[]:
                    input("Actualmente vacia")
                else:
                    clave=int(input("Ingresa id del empleado a borrar: "))
                    for remover in empleados:
                        if remover.idEmpleado == clave:
                            empleados.remove(Empleado(clave,None,None))
                            input("Registro borrado")
            
            elif opcion ==3:
                clave = int(input("Introduce la clave: "))
                if empleados ==[]:
                    input("Actualmente vacia")
                
                else:
                    for remover in empleados:
                        if remover.idEmpleado == clave:
                            remover.nombre = input("Ingrese nuevo nombre: ")
                            remover.direccion = input("Ingrese nueva direccion: ")
                            input("Registro actualizado correctamente.")

            elif opcion == 4:
                print("Ingresa el Id del empleado que desea consultar: ")
                archivo = open("../PIAequipo/empleados.txt","r",encoding="utf8")
                lines = archivo.readlines()
                for line in lines:
                    print (line)
                archivo.close()

            elif opcion == 5:
                if empleados==[]:
                    input("Registro vacio actualmente")
                else:
                    print(f"{'idEmpleado':<20}{'nombre':<20}{'direccion':<20}")

                    for posicion in empleados:
                        print(f"{posicion.idEmpleado:<20}{posicion.nombre:<20}{posicion.direccion:<20}")

            elif opcion == 6:
                break 
            
            elif opcion>6:
                input("Error, introduzca numero del minimenu")

            def guardado():
                archivo=open("./archivos/empleados.txt","w",encoding='utf8')
                for posicion in empleados:
                    archivo.write(str(f" idEmpleado: {posicion.idEmpleado}, nombre: {posicion.nombre}, direccion: {posicion.direccion} ""\n"))
                archivo.close()
            guardado()       