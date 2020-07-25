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


    def borrarEmpleado(self,id):
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
        
    def consultarEmpleado(self):
        #print("Ingresa el Id del empleado que desea consultar: ")
        archivo = open("../PIAequipo/empleados.txt","r",encoding="utf8")
        lines = archivo.readlines()
        for line in lines:
                print (line)
        archivo.close()
    
    def verDetalles(self):
        archivo = open("../PIAequipo/empleados.txt","r",encoding="utf8")  
        id_detalles = input("Ingrese id del empleado: ")
        lines = archivo.readlines()

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


empleado = Empleado("0","dummy","calle sin numero")
while True:
    print("1.-Agregar empleado")
    print("2.-Borrar ")
    print("3.-Modificar")
    print("4.-Consultar")
    print("5.-Ver todos  ")
    print("6.-Salir")
    opcion = int(input("Que opcion eliges?"))

    if opcion == 1:
        print("Agregar empleado")
        break

    elif opcion == 2:
        print("Borrar")   
        break

    elif opcion == 3:
        print("Modificar")   
        break

    elif opcion == 4:
        print("Consultar")   
        empleado.verDetalles()
        break    

    elif opcion == 5:
        print("Ver todos")
        empleado.consultarEmpleado()
        break  
         
    elif opcion == 6:
        print("Salir")   
        break
