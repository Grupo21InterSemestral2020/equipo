from cursos import Cursos
from empleados import Empleado
from temas import Tema
from curso_temas import Curso_Tema
from videos import Video
from curso_temas_videos import Curso_tema_video

while True:
    try:
        opcion=int(input('''
        ¿Donde desea interactuar?
        1)Empleados
        2)Cursos
        3)Temas
        4)Videos
        5)Temas_Curso
        6)VideosAsignados
        7)Salir
        >>Seleccione opcion: '''))
            
        
        if opcion == 1:
            valor=Empleado(0,None,None)
            valor.menu()

        elif opcion == 2:
            valor=Cursos(0,None,None)
            valor.minimenu()

        elif opcion == 3:
            valor=Tema(0,0)
            valor.menu()

        elif opcion == 4:
            valor=Video(0,0,0,0)
            valor.Minimenu()

        elif opcion == 5:
            valor=Curso_Tema(0,0,0)
            valor.menu() 

        elif opcion == 6:
            valor=Curso_tema_video(0,0,0)
            valor.minimenu()    

        elif opcion == 7:
                break


    except ValueError:
        print("Error, introducir unicamente numero")