def floyd_warshall(grafo):
    # grafo: matriz de adyacencia
    n = len(grafo)
    
    # Copiamos la matriz para no modificar el original
    dist = [fila[:] for fila in grafo]

    # Triple ciclo para probar intermediarios k
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

INF = float('inf')

grafo = [
    [0,   2,   5],
    [INF, 0,   1],
    [INF, INF, 0]
]

resultado = floyd_warshall(grafo)
for fila in resultado:
    print(fila)
