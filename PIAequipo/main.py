from cursos import Cursos
from empleados import Empleado
from temas import Tema
from curso_temas import Curso_Tema

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