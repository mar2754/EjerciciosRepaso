lista = [ 1,2,13,45,565,43,76,2,4]
mayor= None
menor= None
for numero in lista:
    if menor==None and mayor==None:
        menor=numero
        mayor=numero
    else:
        if numero<menor:
            menor=numero
        if numero>mayor:
            mayor=numero

print(f"El número mayor es {mayor}")
print(f"El número menor es {menor}")