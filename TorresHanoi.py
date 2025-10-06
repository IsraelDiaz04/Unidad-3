class Pila:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return len(self.elementos) == 0

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            return None

    def cima(self):
        if not self.esta_vacia():
            return self.elementos[-1]
        else:
            return None

    def __str__(self):
        return str(self.elementos)

def mover_disco(origen, destino, nombre_origen, nombre_destino):
    disco = origen.desapilar()
    destino.apilar(disco)
    print(f"Mover disco {disco} de {nombre_origen} → {nombre_destino}")

def hanoi(n, origen, auxiliar, destino, nombre_origen, nombre_aux, nombre_destino):
    if n == 1:
        mover_disco(origen, destino, nombre_origen, nombre_destino)
    else:
        hanoi(n-1, origen, destino, auxiliar, nombre_origen, nombre_destino, nombre_aux)
        mover_disco(origen, destino, nombre_origen, nombre_destino)
        hanoi(n-1, auxiliar, origen, destino, nombre_aux, nombre_origen, nombre_destino)

# Crear pilas
origen = Pila()
auxiliar = Pila()
destino = Pila()

# Colocar los 3 discos en la pila de origen (3 es el más grande)
for disco in [3, 2, 1]:
    origen.apilar(disco)

print("Resolución del juego de las Torres de Hanoi con 3 discos:\n")
hanoi(3, origen, auxiliar, destino, "A", "B", "C")

print("\nEstado final de las torres:")
print("A:", origen)
print("B:", auxiliar)
print("C:", destino)
