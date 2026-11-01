suma = 0
cantidad = 0
nota = 0

while nota != -1:
    nota = float(input("nota (-1 para terminar): "))
    if nota == -1:
        break
    suma += nota
    cantidad += 1
    promedio = suma / cantidad
print("promedio:", promedio)