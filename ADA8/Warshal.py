def warshall(matriz):
    n = len(matriz)
    
    # Copiamos la matriz para no modificar el original
    alcance = [fila[:] for fila in matriz]

    # i = origen
    # j = destino
    # k = intermediario
    for k in range(n):
        for i in range(n):
            for j in range(n):

                # Si puedo ir de i -> k y de k -> j
                # entonces existe camino de i -> j
                if alcance[i][k] == 1 and alcance[k][j] == 1:
                    alcance[i][j] = 1

    return alcance

matriz = [
    [0, 1, 0],  # A -> B
    [0, 0, 1],  # B -> C
    [0, 0, 0]   # C no sale a nadie
]

resultado = warshall(matriz)

for fila in resultado:
    print(fila)
