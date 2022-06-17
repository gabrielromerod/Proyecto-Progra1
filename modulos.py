#Nuestras Funciones
from tabulate import tabulate
import os

#Función para mostrar el menú de opciones
def menu_opcion():
    with open("menu.txt", "r") as abrirMenu:
        print(abrirMenu.read())
    #Pueden encontrar la página de donde saqué
    #la fuente de los títulos aquí:
    #https://patorjk.com/software/taag/#p=display&f=Big&t=Venta%20de%20autos
    while True:
        opcion = input("opcion: ")
        #if opcion < 4 and opcion > 0: 
        if opcion == "1":
            registro_auto()
            enterContinuar()
            break
        elif opcion == "2":
            inventario_auto()
            enterContinuar()
            break
        elif opcion == "3":
            comprar_auto()
            enterContinuar()
            break
        elif opcion == "4":
            exit()
        else:
            print("Introduce una opcion valida, por favor vuelva a intentarlo")

#Registro de autos
def registro_auto():
    try:
        marca = input("Introduce la Marca: ")
        fabricacion = int(input("Introduce el año de Fabricación: "))
        color = input("Introduce el Color: ")
        precio = int(input("Introduce el Precio: "))

    except:
        print("--------------------------------------------------------------------")
        print("Ingresaste un valor erroneo, por favor vuelve a ingresar los datos: ")
        print("--------------------------------------------------------------------")
        registro_auto()
    disponibilidad = "Disponible"
    if os.path.exists("registro.txt"):
        with open("registro.txt", "r") as file:
            contador = 1
            for line in file:
                contador += 1
        registro = "{},{},{},{},{},{}\n".format(contador,marca.lower().capitalize() , fabricacion, color.lower().capitalize() , precio, disponibilidad.lower().capitalize()) #puse esto para que se guarde de manera correcto, creo que debemos encontrar una manera de optimizarlo sin que se vea tan feito
        with open("registro.txt", "a") as file:
            file.write(registro)
    else:
        contador = 1
        registro = "{},{},{},{},{},{}\n".format(contador,marca.lower().capitalize() , fabricacion, color.lower().capitalize() , precio, disponibilidad.lower().capitalize()) #puse esto para que se guarde de manera correcto, creo que debemos encontrar una manera de optimizarlo sin que se vea tan feito
        with open("registro.txt", "a") as file:
            file.write(registro)
    #Fin del programa e interacción con el usuario
    print("\n Registro exitoso !!!")

#Mostrar el inventario de la tienda(los autos disponibles)      
def inventario_auto():
    with open("registro.txt", "r") as lineas:
        listaLineas = []
        listaLineas = (lineas.readlines())
        matrisita = []
        for i in listaLineas:
            lineax = i.split(",")
            matrisita.append(lineax)

        #Imprimo el título
        with open("titulo_autos_disponibles.txt", "r") as file:
            print(file.read())
        
        #Imprimo la tablita
        print(tabulate(matrisita, headers = ["","Marca", "Fabricacion", "Color", "Precio", "Estado"], tablefmt="fancy_grid" ))

#Filtro de selección para comprar auto
def filtrar_por(dato, matriz_ingresada, posicion):
    nueva_matriz = []

    #Filtrar por dato
    for i in range(0, len(matriz_ingresada)):
        if matriz_ingresada[i][posicion] == dato :
            nueva_matriz.append(matriz_ingresada[i])
    #imprimo titulo
    with open("titulo_autos_disponibles.txt", "r") as file:
        print(file.read())
    #Devuelvo la matriz de los autos seleccionados por el usuario
    return nueva_matriz

def comprar_auto():
    #Mostrar título de compra de autos
    with open("compra_de_autos.txt", "r") as abrirCompra_Autos:
        print(abrirCompra_Autos.read())

    #Creación de la nueva matriz que se encargará de los otros datos
    with open("registro.txt", "r") as lineas:
        listaLineas = []
        listaLineas = (lineas.readlines())
        matrisita = []
        for i in listaLineas:
            lineax = i.split(",")
            matrisita.append(lineax)

    #Filtrar datos
    #marca
    marca_seleccionada = input("Introduce la marca del auto que deseas comprar: ")
    marca_seleccionada = marca_seleccionada.lower().capitalize()
    lista_de_auto_a_comprar = filtrar_por(marca_seleccionada, matrisita, 1)
    print(tabulate(lista_de_auto_a_comprar, headers = ["Marca", "Fabricacion", "Color", "Precio", "Estado"], tablefmt="fancy_grid" ))
    si_queda_uno(lista_de_auto_a_comprar)

    #Fabricación
    fabricacion_seleccionada = input("Introduce el año de fabricación del auto que deseas comprar: ")
    fabricacion_seleccionada = fabricacion_seleccionada.lower().capitalize() 
    lista_de_auto_a_comprar = filtrar_por(fabricacion_seleccionada, lista_de_auto_a_comprar, 2)
    print(tabulate(lista_de_auto_a_comprar, headers = ["", "Marca", "Fabricacion", "Color", "Precio", "Estado"], tablefmt="fancy_grid" ))
    si_queda_uno(lista_de_auto_a_comprar)

    #Color
    color_seleccionado = input("Introduce el color seleccionado del auto que deseas comprar: ")
    color_seleccionado = color_seleccionado.lower().capitalize()
    lista_de_auto_a_comprar = filtrar_por(color_seleccionado, lista_de_auto_a_comprar, 3)
    print(tabulate(lista_de_auto_a_comprar, headers = ["", "Marca", "Fabricacion", "Color", "Precio", "Estado"], tablefmt="fancy_grid" ))
    si_queda_uno(lista_de_auto_a_comprar)

    #Precio
    precio_seleccionado = input("Introduce el precio seleccionado del auto que deseas comprar: ")
    precio_seleccionado = precio_seleccionado.lower().capitalize()
    lista_de_auto_a_comprar = filtrar_por(precio_seleccionado, lista_de_auto_a_comprar, 4)
    print(tabulate(lista_de_auto_a_comprar, headers = ["", "Marca", "Fabricacion", "Color", "Precio", "Estado"], tablefmt="fancy_grid" ))
    si_queda_uno(lista_de_auto_a_comprar)

def reemplazar_vendido(file, x):
    temporal = []
    with open(file, 'r') as f:
        contador = 1
        for line in f:
            if contador == x:
                a = line.split(",")
                a[-1] = "Vendido\n"
                b = ",".join(a)
                temporal.append(b)
                contador += 1
            else:
                temporal.append(line)
                contador += 1
    os.remove(file)
    with open(file, 'w') as f:
        for line in temporal:
            f.write(line)

def eliminar_vendido(file):
    temporal = []
    with open(file, 'r') as f:
        contador = 1
        for line in f:
            a = line.split(",")
            if a[-1] == "Vendido\n":
                pass
            else:
                n = a[1:-1]
                b = ",".join(n)
                z = "{},{},Disponible\n".format(contador, b)
                temporal.append(z)
                contador += 1
    os.remove(file)
    with open(file, 'w') as f:
        for line in temporal:
            f.write(line)

def si_queda_uno(auto_a_comprar):
    if len(auto_a_comprar) == 1:
        strauto_a_comprar = ",".join(auto_a_comprar[0])
        strauto_a_comprar = strauto_a_comprar + "\n"

        print("Deseas comprar este auto?: ")
        comprar = input("1.- sí\n2.- Volver al menú\n3.-Salir\nTu respuesta: ")
        if comprar == "1":
            #Codigo reutilizado de "inventario_auto()"
            reemplazar_vendido("registro.txt", int(auto_a_comprar[0][0]))
            print("Gracias por su compra")
            inventario_auto()
            eliminar_vendido("registro.txt")
            enterContinuar()
        elif comprar == "2":
            menu_opcion()
        elif comprar == "3":
            exit()
        else:
            print("Introduce una opción válida")
            print("Deseas comprar este auto?: ")
            comprar = input("1.- sí\n2.- volver\n3.-Salir\nTu respuesta: ")
    elif len(auto_a_comprar) == 0:
        print("Lo sentimos no disponenmos el auto que deseas comprar")
        print("Vuelve a intentarlo")
        enterContinuar()

def enterContinuar():
    a = input("Presiona enter para continuar...")
    a = ""
    if a  == "":
        menu_opcion()

#Programa terminado y optimizado segun la rubrica nwn
