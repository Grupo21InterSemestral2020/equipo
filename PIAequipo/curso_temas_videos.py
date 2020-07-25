class Curso_tema_video:
    def __init__(self,IdCusoTV,IdCT,IdVideo):
        self.__IdCursoTV = IdCusoTV
        self.__IdCT = IdCT
        self.__IdVideo = IdVideo

    @property
    def IdCursoTV(self):
        return self.__IdCursoTV

    @IdCursoTV.setter
    def IdCursoTV(self,valor):
        self.__IdCursoTV = valor

    @property
    def IdCT(self):
        return self.__IdCT

    @IdCT.setter
    def IdCT(self,valor):
        self.__IdCT = valor

    @property
    def IdVideo(self):
        return self.__IdVideo

    @IdVideo.setter
    def IdVideo(self,valor):
        self.__IdVideo = valor 

    def __eq__(self,otro):
        return self.__IdCursoTV == otro.__IdCursoTV
    def minimenu(self):
        limpiar_pantalla()
        lista = []
