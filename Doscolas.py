class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)

    def __str__(self):
        return str(self.items)

def sumar_colas(colaA, colaB):
    colaResultado = Cola()
    while not colaA.esta_vacia() and not colaB.esta_vacia():
        suma = colaA.desencolar() + colaB.desencolar()
        colaResultado.encolar(suma)
    return colaResultado


# Programa principal
colaA = Cola()
colaB = Cola()

n = int(input("¿Cuántos elementos tendrá cada cola? "))

print("Ingrese los elementos de la Cola A:")
for i in range(n):
    valor = int(input(f"Elemento {i+1}: "))
    colaA.encolar(valor)

print("Ingrese los elementos de la Cola B:")
for i in range(n):
    valor = int(input(f"Elemento {i+1}: "))
    colaB.encolar(valor)

colaResultado = sumar_colas(colaA, colaB)

print("\nCola A:", colaA)
print("Cola B:", colaB)
print("Cola Resultado:", colaResultado)
