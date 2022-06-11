import os
 
def reemplazar_vendido(file, x):
    temporal = []
    string = open(file).read()
    with open(file, 'r') as f:
        contador = 1
        for line in f:
            if contador == x:
                a = line.split()
                for z in range(len(a)):
                    if a[z] == "Disponible":
                            a[z] = "Vendido\n"
                b = " ".join(a)
                temporal.append(b)
                contador += 1
            else:
                temporal.append(line)
                contador += 1
    os.remove(file)
    with open(file, 'w') as f:
        for line in temporal:
            f.write(line)

reemplazar_vendido("test.txt", 2)