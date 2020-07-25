class Video:
    def __init__ (self,idVideo,nombre,url,fecha):
        self.__idV = idVideo
        self.__nom = nombre
        self.__url = url
        self.__fechap = fecha

    @property
    def idV(self):
        return self.__idV

    @property
    def url(self):
        return self.__url

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self,valor):
        self.__nom=valor

    @property
    def fechap(self):
        return self.__fechap

    @fechap.setter
    def fechap(self,valor):
        self.__fechap = valor
