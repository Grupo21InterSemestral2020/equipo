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
            limpiar_pantalla()
            lista=[]
            while True:
                try:
                    opcion=int(input("¿Qué Desea hacer?\n1)Agregar\n2)Borrar\n3)Modificar\n4)Consultar\n5)Elegir Clave\n6)Salir\nOpcion:"))
                    if opcion<1:
                        limpiar_pantalla()
                        input("Error, introduzca numero correcto, enter para continuar...")
                    elif opcion==1:
                        limpiar_pantalla()
                        curso=open("./archivos/curso.txt","r")
                        print(curso.read())
                        input("Base de Datos Actual,Enter para continuar...")
                        curso.close()
                        self.__idc=int(input("Ingresa id del curso: "))
                        limpiar_pantalla()
                        tema=open("./archivos/Tema.txt","r")
                        print(tema.read())
                        input("Base de Datos Actual,Enter para continuar...")
                    tema.close()
                    self.__idt=int(input(" Ingresa id del tema: "))
                    limpiar_pantalla()
                    self.__icdt=self.__idct+1
                    valores=Curso_Tema(self.__idct,self.__idc,self.__idt)
                    lista.append(valores)
                    input("Registro Agregado, enter para continuar...")
                    limpiar_pantalla()