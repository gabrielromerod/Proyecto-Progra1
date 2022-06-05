#Archivo Principal de Ejecuación 
import modulos

with open("menu.txt", "r") as abrirMenu:
    print(abrirMenu.read())

modulos.menu_opcion()
