class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

class Arbol:
    def __init__(self, valor_raiz):
        self.raiz = Nodo(valor_raiz)

    def buscar(self, nodo, valor):
        """Busca un nodo por su valor (recursivamente)."""
        if nodo is None:
            return None
        if nodo.valor == valor:
            return nodo
        for hijo in nodo.hijos:
            encontrado = self.buscar(hijo, valor)
            if encontrado:
                return encontrado
        return None

    def insertar(self, valor_padre, valor_hijo):
        """Inserta un nuevo nodo como hijo del valor indicado."""
        nodo_padre = self.buscar(self.raiz, valor_padre)
        if nodo_padre:
            nuevo = Nodo(valor_hijo)
            nodo_padre.hijos.append(nuevo)
            print(f"Nodo '{valor_hijo}' agregado como hijo de '{valor_padre}'.")
        else:
            print(f"⚠️ No se encontró el nodo padre '{valor_padre}'.")

    def preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            for hijo in nodo.hijos:
                self.preorden(hijo)

    def postorden(self, nodo):
        if nodo:
            for hijo in nodo.hijos:
                self.postorden(hijo)
            print(nodo.valor, end=" ")

    def mostrar_hojas(self, nodo):
        if nodo:
            if not nodo.hijos:
                print(nodo.valor, end=" ")
            for hijo in nodo.hijos:
                self.mostrar_hojas(hijo)

    def altura(self, nodo):
        if nodo is None or not nodo.hijos:
            return 1
        return 1 + max(self.altura(hijo) for hijo in nodo.hijos)

    def grado(self, nodo):
        """Devuelve el máximo número de hijos en todo el árbol."""
        if nodo is None:
            return 0
        max_hijos = len(nodo.hijos)
        for hijo in nodo.hijos:
            max_hijos = max(max_hijos, self.grado(hijo))
        return max_hijos

    def nivel(self, nodo, valor, nivel_actual=1):
        if nodo is None:
            return 0
        if nodo.valor == valor:
            return nivel_actual
        for hijo in nodo.hijos:
            nivel_encontrado = self.nivel(hijo, valor, nivel_actual + 1)
            if nivel_encontrado != 0:
                return nivel_encontrado
        return 0

    def nodos_internos(self, nodo):
        if nodo:
            if nodo.hijos:
                print(nodo.valor, end=" ")
            for hijo in nodo.hijos:
                self.nodos_internos(hijo)


def menu():
    print("\n===== MENÚ ÁRBOL =====")
    print("1. Insertar nodo")
    print("2. Mostrar recorrido Preorden")
    print("3. Mostrar recorrido Postorden")
    print("4. Mostrar nodos hoja")
    print("5. Mostrar nodos internos")
    print("6. Mostrar altura del árbol")
    print("7. Mostrar grado del árbol")
    print("8. Mostrar nivel de un nodo")
    print("9. Salir")

# Programa principal
valor_raiz = input("Ingrese el valor de la raíz del árbol: ")
arbol = Arbol(valor_raiz)

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        padre = input("Ingrese el valor del nodo padre: ")
        hijo = input("Ingrese el valor del nuevo nodo hijo: ")
        arbol.insertar(padre, hijo)

    elif opcion == "2":
        print("Recorrido Preorden:")
        arbol.preorden(arbol.raiz)
        print()

    elif opcion == "3":
        print("Recorrido Postorden:")
        arbol.postorden(arbol.raiz)
        print()

    elif opcion == "4":
        print("Nodos hoja:")
        arbol.mostrar_hojas(arbol.raiz)
        print()

    elif opcion == "5":
        print("Nodos internos:")
        arbol.nodos_internos(arbol.raiz)
        print()

    elif opcion == "6":
        print(f"La altura del árbol es: {arbol.altura(arbol.raiz)}")

    elif opcion == "7":
        print(f"El grado del árbol es: {arbol.grado(arbol.raiz)}")

    elif opcion == "8":
        valor = input("Ingrese el valor del nodo: ")
        nivel = arbol.nivel(arbol.raiz, valor)
        if nivel:
            print(f"El nodo '{valor}' está en el nivel {nivel}.")
        else:
            print("Nodo no encontrado.")

    elif opcion == "9":
        print("Saliendo del programa...")
        break

    else:
        print("⚠️ Opción inválida. Intente nuevamente.")
