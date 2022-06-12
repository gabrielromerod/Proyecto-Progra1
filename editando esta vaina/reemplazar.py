import os

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
            print(a)
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

reemplazar_vendido("test.txt",2)
eliminar_vendido("test.txt")