numero = 7
respuesta = input("Adivina el numero: ")
while respuesta != str(numero):
    if respuesta < str(numero):
        print("muy bajo")
        respuesta = input("intenta denuevo: ")
    else:
        print("muy alto")
        respuesta = input("intenta denuevo: ")
print("¡acertaste!")