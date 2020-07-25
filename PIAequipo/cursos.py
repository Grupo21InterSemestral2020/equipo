class Cursos:
    def __init__(self,IdCurso,descripcion,IdEmpleado):
        self.__IdCurso = IdCurso
        self.__descripcion = descripcion
        self.__IdEmpleado = IdEmpleado

    @property
    def IdCurso(self):
        return self.__IdCurso

    @IdCurso.setter
    def IdCurso(self,valor):
        self.__IdCurso = valor

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self,valor):
        self.__descripcion = valor

    @property
    def IdEmpleado(self):
        return self.__IdEmpleado

    @IdEmpleado.setter
    def IdEmpleado(self,valor):
        self.__IdEmpleado = valor

    def __eq__(self,codigo):
       return self.__IdEmpleado = codigo

    def minimenu(self):
        limpiar_pantalla()
        lista =[]

        while true:
            try:
                opcion = int(input("¿Que desea hacer en este apartado?:\n Agregar.\n Borrar.\n Modificar.\n Consultar.\n Elegir Id.\n Salir."))
                if opcion<1:
                    limpiar_pantalla()
                    input("Por favor introduzca numero correcto...")

                elif opcion ==1:
                    limpiar_pantalla()
                    self.__descripcion = int(input("Ingrese la descripcion: "))
                    self.__IdEmpleado = int(input("Ingrese Id del empleado: "))

                    self.__IdCurso = self.__IdCurso+1
                    valores = Cursos(self.__IdCurso,self.__IdCurso,descripcion)
                    lista.append(valores)
                    input("Registro agregado...")
                    limpiar_pantalla()

                elif opcion ==2:
                    limpiar_pantalla()
                    print(f"\n{i1.IdCurso:<30}{i1.descripcion:<30}{i1.IdEmpleado:<30}")
                    for i1 in lista:
                        print(f"{i1.IdCurso:<30}{i1.descripcion:<30}{i1.IdEmpleado:<30}")

                    if lista ==[]:
                        input("Actualmente vacia...")
                        limpiar_pantalla()

                    else:
                        clave = int(input("clave: "))
                        for remover in lista:
                            if remover.IdCurso == clave:
                                lista.remove(Cursos(clave,None,None))
                                input("El registro se ha borrado: ")
                                limpiar_pantalla()

                elif opcion == 3:
                    limpiar_pantalla()
                    print(f"\n {"IdCurso":<30}{"Descripcion":<30}{"IdEmpleado":<30}")

                    for i2 in lista:
                        print(f"{i2.IdCurso:<30}{i2.descripcion:<30}{i2.IdEmpleado:<30}")
                        clave = int(input("clave: "))

                        if lista ==[]:
                            input("Actualmente vacia...")
                            limpiar_pantalla()

                        else:
                            for remover in lista:
                                if remover.IdCurso == clave:
                                    remover.descripcion = int(input("Ingrese la descripcion nueva: "))
                                    remover.IdEmpleado = int(input("Ingrese el nuevo codigo del empleado: "))
                                    print("Informacion registrada exitosamente...")
                                    limpiar_pantalla()
                
                elif opcion ==4:
                    limpiar_pantalla()
                    if lista ==[]:
                        input("Actualmente vacia...")
                        limpiar_pantalla()

                    else:
                        


                            





    
        
        



        


    
