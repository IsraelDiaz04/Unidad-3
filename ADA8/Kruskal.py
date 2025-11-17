class UnionFind:
    def __init__(self, n):
        self.padre = [i for i in range(n)]
        self.rango = [0] * n

    def find(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.find(self.padre[x])
        return self.padre[x]

    def union(self, x, y):
        raizX = self.find(x)
        raizY = self.find(y)

        if raizX != raizY:
            if self.rango[raizX] < self.rango[raizY]:
                self.padre[raizX] = raizY
            elif self.rango[raizX] > self.rango[raizY]:
                self.padre[raizY] = raizX
            else:
                self.padre[raizY] = raizX
                self.rango[raizX] += 1
            return True
        return False


def kruskal(num_nodos, aristas):
    aristas.sort(key=lambda x: x[2])

    uf = UnionFind(num_nodos)
    mst = []

    for u, v, peso in aristas:
        if uf.union(u, v):
            mst.append((u, v, peso))

        if len(mst) == num_nodos - 1:
            break

    return mst


num_nodos = 4
aristas = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

resultado = kruskal(num_nodos, aristas)

print("Aristas del Árbol de Expansión Mínima (MST):")
for u, v, peso in resultado:
    print(f"{u} -- {v}  peso: {peso}")
