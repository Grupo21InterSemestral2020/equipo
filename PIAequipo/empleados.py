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
        
    def menu(self):

        empleados = []
        while True:
            print ("\n1. Agregar empleado\n2.Borrar empleado\n3.Modificar empleado\n4. Ver detalles de empleado\n5.Salir")

            opcion= int(input("Elija una opcion: "))
            if opcion ==1:
                f = open("./PIAequipo/empleados.txt","a",encoding="utf8")
                self.__idEmpleado= self.__idEmpleado+1
                self.__nombre=input("Ingresa el nombre del empleado: ")
                self.__direccion=input("Ingresa la direccion del empleado")
                f.write(self.__idEmpleado,self.__nombre,self.__direccion)
       
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
                clave = int(input("clave: "))
                if empleados ==[]:
                    input("Actualmente vacia")
                
                else:
                    for remover in empleados:
                        if remover.idEmpleado == clave:
                            remover.nombre = input("Ingrese nuevo nombre: ")
                            remover.direccion = input("Ingrese nueva direccion: ")
                            input("Regirstro actualizado correctamente...")



            def guardado():
                archivo=open("./archivos/empleados.txt","w",encoding='utf8')
                for posicion in empleados:
                    archivo.write(str(f" idEmpleado: {posicion.idEmpleado}, nombre: {posicion.nombre}, direccion: {posicion.direccion} ""\n"))
                archivo.close()
            guardado()