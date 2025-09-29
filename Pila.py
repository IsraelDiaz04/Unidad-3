class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return "La pila está vacía"

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return "La pila está vacía"

    def mostrar(self):
        return self.items


if __name__ == "__main__":
    pila = Pila()

    pila.apilar(6)
    pila.apilar(13)
    pila.apilar(42)

    print("Contenido de la pila:", pila.mostrar())
    print("Elemento en la cima:", pila.cima())

    print("Desapilando:", pila.desapilar())
    print("Contenido de la pila:", pila.mostrar()) 
