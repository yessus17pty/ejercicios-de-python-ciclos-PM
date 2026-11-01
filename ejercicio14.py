respuesta = input("escribe hola o salir: ")
while respuesta != "salir":
    if respuesta == "hola":
        print("¡Hola, mucho gusto!")
        respuesta = input("escribe hola o salir: ")
    else:
        print("opcion no valida")
        respuesta = input("escribe hola o salir: ")
print("hasta luego")