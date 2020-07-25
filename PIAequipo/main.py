from cursos import Cursos
from empleados import Empleado
from temas import Tema
from curso_temas import Curso_Tema
from videos import Video

while True:
        try:
            opcion=int(input('''
            ¿Donde desea interactuar?
            1)Empleados
            2)Curso
            3)Temas
            4)Videos
            5)Temas Asignados
            6)VideosAsignados
            7)Salir
            >>Seleccione opcion: "))
            '''
        except ValueError:
            print("Error, ingrese unicamente numero...")

if opcion<1:
    print("Error, ingrese numero valido...")

elif opcion ==1:
    valor = Empleado(0,None,None)
    valor.minimenu()

elif opcion ==2:
    valor = cursos(0,None,None)
    valor.minimenu()