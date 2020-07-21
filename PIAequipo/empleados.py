class Empleado():
    def __init__(self,idEmpleado,nombre,direccion):
        self.__idEmpleado = idEmpleado
        self.__nombre = nombre
        self.__direccion = direccion

    @property
    def id(self):
        return self.__idEmpleado

    @id.setter
    def id(self,idEmp):
        self.__idEmpleado = idEmp 

    @property
    def nombreEmp(self):
        return self.__nombre
    
    @nombreEmp.setter
    def nombreEmp(self,name):
        self.__nombre = name

    @property
    def direccionEmp(self):
        return self.__direccion

    @direccionEmp.setter
    def direccionEmp(self,dirEmp):
        self.__direccion = dirEmp
    