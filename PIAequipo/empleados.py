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
        

    def modificarEmpleado():
        print("Modificacion de parametros: ")
        archivo = open("./PIAequipo/empleados.txt","r",encoding="utf8")
        lines = archivo.readlines()
        archivo.close()
        archivo = open("./PIAequipo/empleados.txt","w",encoding="utf8")
        idEmpleado = input("Ingrese el Id del empleado que desea modificar: ")

        for line in lines:
            id = line.split("|")[0]
            if idEmpleado != id:
                archivo.write(line)

            else:
                print("Ingrese nuevos datos del empleado: ")
                idEmpleado = input("Ingrese id: ")
                nombre = str(input("Ingrese nombre: "))
                direccion = str(input("Ingrese su direccion: "))
                archivo.writelines(idEmpleado + "|" + nombre + "|" + direccion + "|" + "\n" )

        archivo.close()      
        
    def consultarEmpleado():
        print("Ingresa el Id del empleado que desea consultar: ")
        archivo = open("./PIAequipo/empleados.txt","r",encoding="utf8")
        lines = archivo.readlines()
        archivo.close()
    
    def verDetalles(self,id):
        archivo = open("./archi/empleados.txt","r",encoding="utf8")
        lines = archivo.readlines()
        id_detalles = input("Ingrese id del empleado: ")

        for line in lines:
            id = line.split('|')[0]
            if id_detalles == id:
                print (line)
        archivo.close()
        
    def opciones(self):
        empleados = []
        while True:
            print ("""
            1.-Agregar empleado
            2.- Borrar empleado
            3.- Modificar empleado
            4.- Ver detalles de empleado
            5.-Salir""")

            accion= int(input("Elija una opcion: "))
            if accion ==1:
                self.__idEmpleado= self.__idEmpleado+1
                self.__nombre=input("Nombre del empleado: ")
                self.__direccion=input("Direccion del empleado")
                datos=Empleado(self.__idEmpleado,self.__nombre,self.__direccion)
                empleados.append(datos)

<<<<<<< HEAD
=======
            elif accion ==2:
                clave=int(input("Ingrese id del empleado a eliminar: "))
                for remover in empleados:
                    if remover.idEmpleado == clave:
                        empleados.remove(Empleado(clave,None,None))
                        input("Registro borrado")
>>>>>>> 8d8a3be50091cc86a334b36fb1b9339cae477563
