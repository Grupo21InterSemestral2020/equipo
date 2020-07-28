from os import system,name
def limpiar_pantalla():
    if name=='nt':
        system('cls')
    else:
        system('clear')

from cursos import Cursos
from empleados import Empleado
from temas import Tema
from curso_temas import Curso_Tema
from videos import Video
from curso_temas_videos import Curso_tema_video

while True:
    limpiar_pantalla()
    while True:
        try:
            print(f'{"INICIO DE APLICACION":*^30}')
            opcion=int(input("¿Donde desea interactuar?\n1)Empleados\n2)Curso\n3)Temas\n4)Videos\n5)Temas Asignados\n6)VideosAsignados\n7)Salir\n >>Seleccione opcion: "))
            break
        except ValueError:
            limpiar_pantalla()
            input("Error, introducir unicamente numero, vuelva a intentar")
    if opcion<1:
            input("Error, introduzca un numero valido ")
    
    elif opcion==1:
        valor=Empleado(0,None,None)
        valor.menu()   
    elif opcion==2:
        valor=Cursos(0,None,None)
        valor.minimenu()
    elif opcion==3:
        valor=Tema(0,0)
        valor.menu()
    elif opcion==4:
        valor=Video(0,0,0,0)
        valor.Minimenu()
    elif opcion==5:
        valor=Curso_Tema(0,0,0)
        valor.Minimenu()
    elif opcion==6:
        valor=Curso_tema_video(0,0,0)
        valor.minimenu()
    elif opcion==7:
        limpiar_pantalla()
        break
    elif opcion>7:
        input("Error, introduzca un numero valido")