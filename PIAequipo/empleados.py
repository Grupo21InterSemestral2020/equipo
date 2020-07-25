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
            print ("\n1. Agregar empleado\n2.Borrar empleado\n3.Modificar empleado\n4. Ver detalles de empleado\n5.Salir")

            opcion= int(input("¿Que accion desea ejecutar:"))
            if opcion ==1:
                self.__idEmpleado= self.__idEmpleado+1
                self.__nombre=input("Ingresa el nombre del empleado: ")
                self.__direccion=input("Ingresa la direccion del empleado")
                datos=Empleado(self.__idEmpleado,self.__nombre,self.__direccion)
                empleados.append(datos)
       
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