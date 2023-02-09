def sumar_lista(lista):

    suma = 0

    for numero in lista:
        suma += numero

    return suma


numeros = [2, 4, 6, 8, 10]

print(sumar_lista(numeros))
