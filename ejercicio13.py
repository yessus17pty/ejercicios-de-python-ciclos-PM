palabra = input("escribe una palabra: ")
contador = 0
for letra in palabra.lower():
    if letra in "aeiou":
        contador += 1
print("tiene", contador, "vocales")