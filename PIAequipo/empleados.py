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
    
    def addEmpleado(self,idEmpleado,nombre,direccion,f):
        f = open("./PIAequipo/empleados.txt","a",encoding="utf8")
        idEmpleado = int(input("Ingresa id de empleado: "))
        nombre = input("Ingresa nombre del empleado: ")
        direccion = input("Direccion del empleado:")
        f.write(str(idEmpleado) + "|" + nombre + "|" + direccion + "\n")
        f.close()

    def opciones(self,opc):
        print(" 1 - Agregar empleado")
        print(" 2 - Borrar empleado")
        print(" 3 - Modificar empleado")
        print(" 4 - Consultar empleado")
        print(" 5 - Ver detalles de empleado")
        print(" 6 - Salir")
        opc = int(input("Seleccione opcion: "))
        if opc == 1:
            addEmpleado()