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
    
    def agregarEmpleado(self,idEmpleado,nombre,direccion,f):
        f = open("./PIAequipo/empleados.txt","a",encoding="utf8")
        idEmpleado = int(input("Ingresa id de empleado: "))
        nombre = input("Ingresa nombre del empleado: ")
        direccion = input("Direccion del empleado:")
        f.write(str(idEmpleado) + "|" + nombre + "|" + direccion + "\n")
        f.close()


    def borrarEmpleado():
        archivo = open("./PIAequipo/empleados.txt","r",encoding="utf8")
        lines = archivo.readlines()
        archivo.close()
        archivo = open("./PIAequipo/empleados.txt","w",encoding="utf8")
        idEmpleado = input("Ingrese Id que desea eliminar: ")

        for line in lines:
            id = line.split("|")[0]
            if idEmpleado != id:
                archivo.write(line)
        archivo.close()     
           

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
        archivo = open("./PIAequipo/empleados.txt","r",encoding="utf8")
        lines = archivo.readlines()
        id_detalles = input("Ingrese id del empleado: ")

        for line in lines:
            id = line.split('|')[0]
            if id_detalles == id:
                print (line)
        archivo.close()
        
    
    def opciones(self,opc):
        print(" 1 - Agregar empleado")
        print(" 2 - Borrar empleado")
        print(" 3 - Modificar empleado")
        print(" 4 - Consultar empleado")
        print(" 5 - Ver detalles de empleado")
        print(" 6 - Salir")
        opc = int(input("Seleccione opcion: "))
        if opc == 1:
            agregarEmpleado()
        elif opc == 2:
            borrarEmpleado()
        elif opc == 3:
            modificarEmpleado()
        elif opc == 4:
            consultarEmpleado()
        elif opc == 5:
            detallesEmpleado()
        elif opc == 6:
            salir()   
    



    

    
            