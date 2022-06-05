#Nuestras Funciones
import time
from tabulate import tabulate
#Le preguntamos al usuario si quiere seguir corriendo el programa
def pregunta():
    print("\n\nQuieres seguir usando el programa? ")
    si_o_no = input("Escribe sí o no para responder: ")
    si_o_no = si_o_no.lower()
    while True:
        if si_o_no == "si" or si_o_no == "sí":
            menu_opcion()
        elif si_o_no == "no":
            exit()
        else:
            print("Ingresa una respuesta válida >:C")
            si_o_no = input("Quieres seguir usando el programa?: ")

#Le mostramos nuestro menú de opciones
def menu_opcion():
    with open("menu.txt", "r") as abrirMenu:
        print(abrirMenu.read())
    #Pueden encontrar la página de donde saqué
    #la fuente del título aquí:
    #https://patorjk.com/software/taag/#p=display&f=Big&t=Venta%20de%20autos
    while True:
        opcion = int(input("opcion: "))
        #if opcion < 4 and opcion > 0: 
        id = 0
        if opcion == 1:
            id += 1
            registro_auto(id)
            break
        elif opcion == 2:
            inventario_auto()
            break
        elif opcion == 3:
            compra_auto()
            break
        else:
            print("Introduce una opcion valida, por favor vuelva a intentarlo")


#Registro de autos
def registro_auto(identificador):
    marca = input("Introduce la Marca: ")
    fabricacion = int(input("Introduce el año de Fabricación: "))
    color = input("Introduce el Color: ")
    precio = int(input("Introduce el Precio: "))
    disponibilidad = "Disponible"
    registro = "{} {} {} {} {} {}\n".format(identificador, marca.lower().capitalize(), fabricacion, color.lower().capitalize(), precio, disponibilidad.lower().capitalize()) #puse esto para que se guarde de manera correcto, creo que debemos encontrar una manera de optimizarlo sin que se vea tan feito
    with open("registro.txt", "a") as file:
        file.write(registro)
    #Fin del programa e interacción con el usuario
    print("\n Registro exitoso !!!")
    pregunta()


#Mostrar el inventario de la tienda(los autos disponibles)      
def inventario_auto():
    with open("registro.txt", "r") as lineas:
        listaLineas = []
        listaLineas = (lineas.readlines())
        matrisita = []
        for i in listaLineas:
            lineax = i.split()
            matrisita.append(lineax)

        #Imprimo la tablita
        print(tabulate(matrisita, headers = ["", "Marca", "Fabricacion", "Color", "Precio", "Estado"], tablefmt="fancy_grid" ))
    print("\n Estos son todos los autos que tenemos!!")
    print("Te animas a comprar?")
    pregunta()#Le preguntamos al usuario si quiere seguir corriendo el programa


#Comprar un auto
def compra_auto():
    print("compra de autoss")
    print("bla bla bla")
    opcion = int(input("Introduce el ID de uno de nuestros autos: "))
    for i in range(0, len(opcion)):
        pass
    
    


