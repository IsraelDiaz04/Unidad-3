class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return None

    def __len__(self):
        return len(self.items)


class SistemaSeguros:
    def __init__(self):
        # Cada servicio tiene su propia cola
        self.colas = {
            1: Cola(),  # Ejemplo: Servicio de autos
            2: Cola(),  # Ejemplo: Servicio de vida
            3: Cola()   # Ejemplo: Servicio de salud
        }
        self.contadores = {1: 0, 2: 0, 3: 0}

    def llegada_cliente(self, servicio):
        if servicio not in self.colas:
            print("Ventanilla no válido.")
            return
        self.contadores[servicio] += 1
        numero = self.contadores[servicio]
        self.colas[servicio].encolar(numero)
        print(f"Cliente agregado a ventanilla {servicio}. Número de atención: {numero}")

    def atender_cliente(self, servicio):
        if servicio not in self.colas:
            print("Servicio no válido.")
            return
        if self.colas[servicio].esta_vacia():
            print(f"No hay clientes en la ventanilla {servicio}.")
        else:
            numero = self.colas[servicio].desencolar()
            print(f"Atendiendo cliente número {numero}, ventanilla {servicio}.")


def main():
    sistema = SistemaSeguros()
    print("Sistema de atención - Compañía de Seguros")
    print("BIENVENIDOS AL MENU:")
    print("  C#  → llegada de cliente (ejemplo: C1, pone al Cliente en la ventanilla 1)")
    print("  A#  → atender cliente (ejemplo: A2, el cliente de la ventanilla 2)")
    print("  S   → salir")

    while True:
        comando = input("\nIngrese comando: ").strip().upper()
        if comando == "S":
            print("Saliendo del sistema...")
            break
        elif comando.startswith("C"):
            try:
                servicio = int(comando[1])
                sistema.llegada_cliente(servicio)
            except:
                print("Comando inválido. Use formato C#")
        elif comando.startswith("A"):
            try:
                servicio = int(comando[1])
                sistema.atender_cliente(servicio)
            except:
                print("Comando inválido. Use formato A#")
        else:
            print("Comando no reconocido.")


if __name__ == "__main__":
    main()
