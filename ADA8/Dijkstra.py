import heapq

def dijkstra(grafo, origen):
    # Inicializamos distancias como infinito
    dist = {nodo: float('inf') for nodo in grafo}
    dist[origen] = 0

    # Cola de prioridad (distancia, nodo)
    cola = [(0, origen)]

    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)

        # Si esta distancia no es la mejor, la ignoramos
        if distancia_actual > dist[nodo_actual]:
            continue

        # Revisamos vecinos
        for vecino, peso in grafo[nodo_actual]:
            nueva_dist = distancia_actual + peso

            # Si encontramos un camino más corto
            if nueva_dist < dist[vecino]:
                dist[vecino] = nueva_dist
                heapq.heappush(cola, (nueva_dist, vecino))

    return dist

#USO
grafo = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('C', 1), ('D', 3)],
    'C': [('A', 5), ('B', 1), ('D', 2)],
    'D': [('B', 3), ('C', 2)]
}

resultado = dijkstra(grafo, 'A')
print(resultado)
