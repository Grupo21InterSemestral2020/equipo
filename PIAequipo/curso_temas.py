from os import system,name
def limpiar_pantalla():
    if name=='nt':
        system('cls')
    else:
        system('clear')
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

    @property
    def idt(self):
        return self.__idt

    @idc.setter
    def idc(self,valor):
        self.__idc=valor
    
    @idt.setter
    def idt(self,valor):
        self.__idt=valor

    @idct.setter
    def idct(self,valor):
        self.__idct=valor    

    def menu(self):
        limpiar_pantalla()
        lista=[]
        while True:
            try:
                opcion=int(input('''
                CURSO TEMAS :Elija la opcion que desea
                1)Agregar
                2)Borrar
                3)Modificar
                4)Consultar todo
                5)Ver detalles
                6)Salir
                >>Opcion:'''))
                if opcion<1:
                    limpiar_pantalla()
                    input("Error, introduzca opcion valida")

                elif opcion==1:
                    limpiar_pantalla
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
                    limpiar_pantalla()
                    self.__icdt=self.__idct+1
                    valores=Curso_Tema(self.__idct,self.__idc,self.__idt)
                    lista.append(valores)
                    input("Empleado Agregado")
                    limpiar_pantalla()

                elif opcion==2:
                    limpiar_pantalla()
                    print(f"\n{'idCursoTema':<30}{'idCurso':<30}{'idTema':<30}")
                    for i1 in lista:
                        print(f"{i1.idct:<30}{i1.idc:<30}{i1.idt:<30}")
                    if lista==[]:
                        input("Registro vacio")
                        limpiar_pantalla()
                    else:
                        clave=int(input("Ingresa clave:"))
                    for remover in lista:
                        if remover.idct == clave:
                            lista.remove(Curso_Tema(clave,None,None))
                            input("Registro borrado")
                            limpiar_pantalla
                
                elif opcion==3:
                    limpiar_pantalla()
                    print(f"\n{'idCursoTema':<30}{'idCurso':<30}{'idTema':<30}")
                    for i2 in lista:
                        print(f"{i2.idct:<30}{i2.idc:<30}{i2.idt:<30}")
                    clave=int(input("Ingresa la clave:"))
                    if lista==[]:
                        print("Registro vacio")
                        limpiar_pantalla()
                    else:
                        for remover in lista:
                            if remover.ict==clave:
                                remover.ic=int(input("Ingresa el curso nuevo: "))
                                remover.it=int(input("Ingresa el tema nuevo: "))
                                input("Registro Actualizado")
                elif opcion==4:
                    limpiar_pantalla()
                    if lista==[]:
                        input("Registro vacio")
                        limpiar_pantalla()
                    else:
                        print(f"\n{'idCursoTema':<30}{'idCurso':<30}{'idTema':<30}")
                        for i3 in lista:
                            print(f"{i3.idct:<30}{i3.idc:<30}{i3.idt:<30}")
                            limpiar_pantalla()
                
                elif opcion==5:
                    limpiar_pantalla()
                    print(f"\n{'idCursoTema':<30}{'idCurso':<30}{'idTema':<30}")
                    for i4 in lista:
                        print(f"{i4.idct:<30}{i4.idc:<30}{i4.idt:<30}")
                    clave=int(input("Ingrese clave:"))
                    limpiar_pantalla()
                    print(f"\n{'idCursoTema':<30}{'idCurso':<30}{'idTema':<30}")
                    for i5 in lista:
                        if i5.idct==clave:
                            print(f"{i5.idct:<30}{i5.idc:<30}{i5.idt:<30}")

                elif opcion==6:
                    break
                elif opcion>6:
                    input("Error, introduzca opcion valida")
                    limpiar_pantalla()
                
                def informacion():
                    archivo=open("./archivos/Curso_Temas.txt","w",encoding='utf8')
                    for i6 in lista:
                        archivo.write(str(f" IdCursoTema: {i6.idct}, IdCurso: {i6.idc}, IdTema: {i6.idt}""\n"))
                    archivo.close()
                informacion()
            except ValueError:
                input("Error, introduzca solo numero de opcion valida del menu")
 