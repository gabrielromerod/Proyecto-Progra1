#Nuestras Funciones
from tabulate import tabulate

#Función para preguntarle al usuario si quiere seguir corriendo el programa
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


#Función para mostrar el menú de opciones
def menu_opcion():
    with open("menu.txt", "r") as abrirMenu:
        print(abrirMenu.read())
    #Pueden encontrar la página de donde saqué
    #la fuente del título aquí:
    #https://patorjk.com/software/taag/#p=display&f=Big&t=Venta%20de%20autos
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
            comprar_auto()
            break
        else:
            print("Introduce una opcion valida, por favor vuelva a intentarlo")


#Registro de autos
def registro_auto():
    marca = input("Introduce la Marca: ")
    fabricacion = int(input("Introduce el año de Fabricación: "))
    color = input("Introduce el Color: ")
    precio = int(input("Introduce el Precio: "))
    disponibilidad = "Disponible"
    registro = "{} {} {} {} {}\n".format(marca.lower().capitalize(), fabricacion, color.lower().capitalize(), precio, disponibilidad.lower().capitalize()) #puse esto para que se guarde de manera correcto, creo que debemos encontrar una manera de optimizarlo sin que se vea tan feito
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
        print(tabulate(matrisita, headers = ["Marca", "Fabricacion", "Color", "Precio", "Estado"], tablefmt="fancy_grid" ))
    print("\nEstos son todos los autos que tenemos!!")
    print("Te animas a comprar?")
    pregunta()#Le preguntamos al usuario si quiere seguir corriendo el programa


#Seleccionar el auto
def filtrar_por(marca, matriz_ingresada, posicion):

    #Nueva matriz
    nueva_matriz = []

    #Filtrar por Marca
    for i in range(0, len(matriz_ingresada)):

        if matriz_ingresada[i][posicion] == marca :
            nueva_matriz.append(matriz_ingresada[i])

    #imprimo la lista de autos seleccionada por el usuario tabulada bonita uwu
    print("Estos son nuestros autos de la marca",marca, "\n")
    print(tabulate(nueva_matriz, headers = ["Marca", "Fabricacion", "Color", "Precio", "Estado"], tablefmt="fancy_grid" ))


def comprar_auto():
    #Mostrar título de compra de autos
    with open("compra_de_autos.txt", "r") as abrirCompra_Autos:
        print(abrirCompra_Autos.read())

    marca_seleccionada = input("Introduce la marca del auto que deseas comprar: ")
    marca_seleccionada = marca_seleccionada.lower().capitalize() 

    #Creación de la nueva matriz que se encargará de filtrar los datos
    with open("registro.txt", "r") as lineas:
        listaLineas = []
        listaLineas = (lineas.readlines())
        matrisita = []
        for i in listaLineas:
            lineax = i.split()
            matrisita.append(lineax)

    
    filtrar_por(marca_seleccionada, matrisita, 0)
    filtrar_por(marca_seleccionada, matrisita, 1)
    filtrar_por(marca_seleccionada, matrisita, 2)
    filtrar_por(marca_seleccionada, matrisita, 3)















#Prevención de casos 1(si solo hay un vehiculo disponible, se le pregunta si desea comprarlo)
# if len(nueva_matriz) == 1:
#     #Sí, reutilicé el código de "pregunta()"
#     print("Estos son nuestros autos de la marca", marca_seleccionada, "\n")
#     print(tabulate(nueva_matriz, headers = ["Marca", "Fabricacion", "Color", "Precio", "Estado"], tablefmt="fancy_grid" ))

#     #Desea comprar el auto?
#     si_o_no = input("Quieres comprar este auto?: ")
#     si_o_no = si_o_no.lower()
#     while True:
#         if si_o_no == "si" or si_o_no == "sí":
#             comprar_auto()
#             break
#         elif si_o_no == "no":
#             print("Vuelve cuando quierass!")
#             pregunta()
#         else:
#             print("Ingresa una respuesta válida >:C")
#             si_o_no = input("Quieres comprar este auto?: ")
# else:
#     print("Esta marca no está disponible")
#     pregunta()