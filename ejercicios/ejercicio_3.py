import random
def listaAleatorios(n):
      lista = [0]  * n
      for i in range(n):
          lista[i] = random.random()
      return lista

print("Ingrese cuantos numeros aleatorios desea obtener")
n=int(input())

aleatorios=listaAleatorios(n)
print(aleatorios)