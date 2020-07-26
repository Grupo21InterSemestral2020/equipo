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
    def IdEmpleado(self,codigo):
        self.__IdEmpleado = codigo

    
    
    def __eq__(self,otro):
       return self.__IdCurso == otro.__IdCurso

    def minimenu(self):
        lista =[]
        while True:
            try:
                opcion = int(input('''
                ¿Que desea hacer en este apartado?:
                1)Agregar
                2)Borrar
                3)Modificar
                4)Consultar
                5)Elegir Id
                6)Salir'''))
                if opcion < 1:
                   input("Por favor introduzca numero correcto...")
                    

                elif opcion == 1:
                    self.__descripcion = input("Ingrese la descripcion: ")
                    self.__IdEmpleado = int(input("Ingrese Id del empleado: "))
                    self.__IdCurso = self.__IdCurso + 1
                    valores = Cursos(self.__IdCurso,self.__descripcion,self.__IdCurso)
                    lista.append(valores)
                    input("Registro agregado")

                    
                    

                elif opcion == 2:
                    print(f"\n{'IdCurso':<30}{'descripcion':<30}{'IdEmpleado':<30}")
                    for i1 in lista:
                        print(f"{i1.IdCurso:<30}{i1.descripcion:<30}{i1.IdEmpleado:<30}")

                    if lista ==[]:
                        input("Actualmente vacia...")
                    
                    else:
                        clave = int(input("clave: "))
                        for remover in lista:
                            if remover.IdCurso == clave:
                                lista.remove(Cursos(clave,None,None))
                                input("El registro se ha borrado: ")    

                elif opcion == 3:
                    print(f"\n{'IdCurso':<30}{'descripcion':<30}{'IdEmpleado':<30}")
                    for i2 in lista:
                        print(f"{i2.IdCurso:<30}{i2.descripcion:<30}{i2.IdEmpleado:<30}")
                        clave = int(input("clave: "))

                        if lista ==[]:
                            input("Actualmente vacia...")
                        else:
                            for remover in lista:
                                if remover.IdCurso == clave:
                                    remover.descripcion = int(input("Ingrese la descripcion nueva: "))
                                    remover.IdEmpleado = int(input("Ingrese el nuevo codigo del empleado: "))
                                    print("Informacion registrada exitosamente...")
                   
                                    
                
                elif opcion == 4:
                    if lista ==[]:
                        input("Actualmente vacia...")

                    else:
                        print(f"\n{'IdCurso':<30}{'descripcion':<30}{'IdEmpleado':<30}")
                        
                        for i3 in lista:
                            print(f"{i3.IdCurso:<30}{i3.descripcion:<30}{i3.IdEmpleado:<30}")
                            input("Pulse enter para continuar...")       

                    
                elif opcion == 5:
                        print(f"\n{'IdCurso':<30}{'descripcion':<30}{'IdEmpleado':<30}")
                        
                        for i4 in lista:
                            print(f"{i4.IdCurso:<30}{i4.descripcion:<30}{i4.IdEmpleado:<30}")
                            clave = int(input("clave: "))
                        
                        print(f"\n{'IdCurso':<30}{'descripcion':<30}{'IdEmpleado':<30}")
                        
                        for i5 in lista:
                            if i5.IdCurso == clave:
                                print(f"{i5.IdCurso:<30}{i5.descripcion:<30}{i5.IdEmpleado:<30}")
                                input("Pulse enter para continuar...")
                 
                 
                elif opcion == 6:
                    break
                elif opcion>6:
                    input("Numero no valido, favor de registrar numero valido...")
                    
                    def Informacion():
                        archivo = open("./PIAequipo/cursos.txt","w",encoding='utf8')
                        for i6 in lista:
                            archivo.write(str(f"IdCurso: {i6.IdCurso}, descripcion: {i6.descripcion}, IdEmpleado: {i6.IdEmpleado}""\n"))
                        archivo.close()
                        Informacion()

            except ValueError:
                print("Introducir unicamente numero...")
                
                    

                            
                        


                            





    
        
        



        


    
