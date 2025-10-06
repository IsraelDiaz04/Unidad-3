class Pila:
    def __init__(self, capacidad):
        self.elementos = []
        self.capacidad = capacidad

    def mostrar_pila(self):
        print("Estado actual de la pila:")
        if not self.elementos:
            print("[VACÍA]")
        else:
            for i in reversed(self.elementos):
                print(f"| {i} |")
        print("‾‾‾‾‾‾‾‾‾‾")
        print(f"TOPE = {len(self.elementos)}\n")

    def insertar(self, dato):
        print(f"Insertar({dato})")
        if len(self.elementos) < self.capacidad:
            self.elementos.append(dato)
        else:
            print(f"Error: Desbordamiento. No se puede insertar {dato}.")
        self.mostrar_pila()

    def eliminar(self, nombre):
        print(f"Eliminar({nombre})")
        if len(self.elementos) > 0:
            eliminado = self.elementos.pop()
            print(f"Se eliminó: '{eliminado}'")
        else:
            print(f"Error: Subdesbordamiento al intentar eliminar {nombre}.")
        self.mostrar_pila()


# Simulación del problema
pila = Pila(8)

pila.insertar("X")
pila.insertar("Y")
pila.eliminar("Z")
pila.eliminar("T")
pila.eliminar("U")
pila.insertar("V")
pila.insertar("W")
pila.eliminar("p")
pila.insertar("R")

print("Contenido final de la pila:", pila.elementos)
print("Cantidad de elementos:", len(pila.elementos))
