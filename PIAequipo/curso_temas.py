class Curso_Tema:
    def __init__(self, idCursoTema,idCurso,idTema):
        self.__idct=idCursoTema
        self.__idc=idCurso
        self.__idt=idTema
    @property
    def idct(self):
        return self.__idct
    @property
    def idc(self):
        return self.__idc
    @idc.setter
    def idc(self,valor):
        self.__idc=valor
    @property
    def it(self):
        return self.__idt
    @idt.setter
    def idt(self,valor):
        self.__idt=valor

    def menu(self):
        lista=[]
        while True:
            try:
                opcion=int(input("¿Qué Desea hacer?\n1)Agregar\n2)Borrar\n3)Modificar\n4)Consultar\n5)Elegir Clave\n6)Salir\nOpcion:"))
                if opcion<1:
                    input("Error, introduzca opcion valida")

                elif opcion==1:
                    curso=open("./archivos/curso.txt","r")
                    print(curso.read())
                    input("Base de Datos Actual")
                    curso.close()
                    self.__idc=int(input("Ingresa id del curso: "))
                    tema=open("./archivos/Tema.txt","r")
                    print(tema.read())
                    input("Base de Datos Actual")
                    tema.close()
                    self.__idt=int(input("Ingresa id del tema: "))
                    self.__icdt=self.__idct+1
                    valores=Curso_Tema(self.__idct,self.__idc,self.__idt)
                    lista.append(valores)
                    print("Empleado Agregado")

                elif opcion==2:
                    print(f"\n{'idCursoTema':<30}{'idCurso':<30}{'idTema':<30}")
                    for i1 in lista:
                        print(f"{i1.idct:<30}{i1.idc:<30}{i1.idt:<30}")
                    if lista==[]:
                        input("Registro vacio")
                    else:
                        clave=int(input("Clave:"))
                    for remover in lista:
                        if remover.idct == clave:
                            lista.remove(Curso_Tema(clave,None,None))
                            input("Registro borrado")
                elif opcion==3:
                    print(f"\n{'idCursoTema':<30}{'idCurso':<30}{'idTema':<30}")
                    for i2 in lista:
                        print(f"{i2.idct:<30}{i2.idc:<30}{i2.idt:<30}")
                    clave=int(input("Ingresa la clave:"))
                    if lista==[]:
                        print("Registro vacio")
                    else:
                        for remover in lista:
                            if remover.ict==clave:
                                remover.ic=int(input("Ingresa el curso nuevo: "))
                                remover.it=int(input("Ingresa el tema nuevo: "))
                                input("Registro Actualizado")
                elif opcion==4:
                    if lista==[]:
                        input("Registro vacio")
                    else:
                        print(f"\n{'idCursoTema':<30}{'idCurso':<30}{'idTema':<30}")
                        for i3 in lista:
                            print(f"{i3.ict:<30}{i3.ic:<30}{i3.it:<30}")
                        input("Enter para continuar...")