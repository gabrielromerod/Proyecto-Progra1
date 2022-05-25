#Nuestras Funciones
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

def compra_auto():
    1

