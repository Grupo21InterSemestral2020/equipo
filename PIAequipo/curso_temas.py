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