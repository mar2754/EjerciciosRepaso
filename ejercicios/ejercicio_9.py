def carga_matriz(filas, columnas, vector):
    for i in range(filas):
        vector.append([0] * columnas)
        for j in range(columnas):
            vector[i][j] = input("Ingrese los elementos: ")
    print(vector, filas, columnas)
    # return f, c


f = int(input("Ingrese la cantidad de filas: "))
c = int(input("Ingrese la cantidad de columnas: "))
v = []
carga_matriz(f, c, v)