#Nuestras Funciones
from re import M


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
    disponibilidad = 1
    registro = "{};{};{};{};{}\n".format(marca, fabricacion, color, precio,disponibilidad)
    with open("registro.txt", "a") as file:
        file.write(registro)

def inventario_auto():
    marca_lista = []
    fabricacion_lista = []
    color_lista = []
    precio_lista = []
    disponibilidad_lista = []
    with open("registro.txt") as file:
        for line in file:
            caracter = str(line)
            registro = 0
            marca = ""
            fabricacion = ""
            color = ""
            precio = ""
            disponibilidad = ""
            for caracter in line:
                if caracter == ";":
                    registro += 1
                elif registro == 0:
                    marca += caracter
                elif registro == 1:
                    fabricacion += caracter
                elif registro == 2:
                    color += caracter
                elif registro == 3:
                    precio += caracter
                elif registro == 4:
                    disponibilidad += caracter
            precio_int = int(precio)
            disponibilidad_int = int(disponibilidad)
            fabricacion_int = int(fabricacion)     
            marca_lista.append(marca)
            fabricacion_lista.append(fabricacion_int)
            color_lista.append(color)
            precio_lista.append(precio_int)
            disponibilidad_lista.append(disponibilidad_int)
        
    recorredor = 0
    print("{a1}               {a2}         {a3}               {a4}              {a5}              ".format(a1="MARCA",a2="FABRICACION",a3="COLOR",a4="PRECIO", a5="ESTADO"))
    while not recorredor == len(marca_lista):
        if disponibilidad_lista[recorredor] == 1:
            vacio = " "
            total = 20 - len(marca_lista[recorredor])
            espacios = vacio * total
            print("{}{}".format(marca_lista[recorredor], espacios), end="")
            vacio = " "
            total = 20 - len(str(fabricacion_lista[recorredor]))
            espacios = vacio * total
            print("{}{}".format(fabricacion_lista[recorredor], espacios),end="")
            vacio = " "
            total = 20 - len(color_lista[recorredor])
            espacios = vacio * total
            print("{}{}".format(color_lista[recorredor], espacios), end="")
            vacio = " "
            total = 20 - len(str(precio_lista[recorredor]))
            espacios = vacio * total
            print("{}{}".format(precio_lista[recorredor], espacios), end="")
            total = 20 - len(str("disponible"))
            espacios = vacio * total
            print("{a1}".format(a1="disponible"))
            recorredor += 1
        else:
            recorredor += 1

def compra_auto():
    marca_lista = []
    fabricacion_lista = []
    color_lista = []
    precio_lista = []
    disponibilidad_lista = []
    with open("registro.txt") as file:
        for line in file:
            caracter = str(line)
            registro = 0
            marca = ""
            fabricacion = ""
            color = ""
            precio = ""
            disponibilidad = ""
            for caracter in line:
                if caracter == ";":
                    registro += 1
                elif registro == 0:
                    marca += caracter
                elif registro == 1:
                    fabricacion += caracter
                elif registro == 2:
                    color += caracter
                elif registro == 3:
                    precio += caracter
                elif registro == 4:
                    disponibilidad += caracter
            precio_int = int(precio)
            disponibilidad_int = int(disponibilidad)
            fabricacion_int = int(fabricacion)     
            marca_lista.append(marca)
            fabricacion_lista.append(fabricacion_int)
            color_lista.append(color)
            precio_lista.append(precio_int)
            disponibilidad_lista.append(disponibilidad_int)

    with open("registro.txt", "r+") as file:
        while True: #filtrar data para saber si existen o no
            marca_comprar = input("Marca: ")
            fabricacion_comprar = int(input("Fabricacion: "))
            color_comprar = input("Color: ")
            precio_comprar = int(input("Precio: "))
            if marca_comprar in marca_lista and fabricacion_comprar in fabricacion_lista and color_comprar in color_lista and precio_comprar in precio_lista:
                break
            else:
                print("Por favor revise los datos de entrada")
        indice = marca_lista.index(marca_comprar) + 1
        contador = 1                                
        #NO FUNCIONA NADA DE ACA ABAJO NOS CANSAMOS 
        for line in file:
            print(line)
            if contador == indice:
                line.write(line.replace([-1],"0"))
            contador += 1