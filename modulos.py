#Nuestras Funciones
import pandas as pd
from tabulate import tabulate

def menu_opcion():
    while True:
        opcion = int(input("opcion: "))
        #if opcion < 4 and opcion > 0: 
        if opcion == 1:
            registro_auto()
            break
        elif opcion == 2:
            inventario_auto()
            break
        elif opcion == 3:
            compra_auto()
            break
        else:
            print("Introduce una opcion valida, por favor vuelva a intentarlo")

def registro_auto():
    marca = input("Marca: ")
    fabricacion = int(input("Fabricación: "))
    color = input("Color: ")
    precio = int(input("Precio: "))
    disponibilidad = "Disponible"

    registro = "{} {} {} {} {}\n".format(marca.lower().capitalize(), fabricacion.lower().capitalize(), color.lower().capitalize(), precio.lower().capitalize(), disponibilidad.lower().capitalize()) #puse esto para que se guarde de manera correcto, creo que debemos encontrar una manera de optimizarlo sin que se vea tan feito
    with open("registro.txt", "a") as file:
        file.write(registro)
        

def inventario_auto():
    with open("registro.txt", "r") as lineas:
        listaLineas = []
        listaLineas = (lineas.readlines())
        matriz = []

        for i in listaLineas:
            lineax = i.split()
            matriz.append(lineax)

        #Estoy creando un DataFrame de la matriz
        data_frame = pd.DataFrame(matriz, columns= ["Marca", "Fabricacion", "Color", "Precio", "Disponibilidad"] )
        print(tabulate(data_frame, headers = ["Marca", "Fabricacion", "Color", "Precio", "Disponibilidad"], tablefmt="pretty" ))

def compra_auto():
    pass
