# my_linked_list.py

class Node:
    """Clase que representa un nodo individual de la lista enlazada."""
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    """Implementación personalizada de una lista enlazada simple."""
    def __init__(self):
        self.head = None

    def is_empty(self):
        """Verifica si la lista está vacía."""
        return self.head is None

    def insert_at_beginning(self, data):
        """Inserta un nuevo nodo al inicio de la lista."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Inserta un nuevo nodo al final de la lista."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after(self, prev_data, data):
        """Inserta un nuevo nodo después de un valor existente."""
        current = self.head
        while current and current.data != prev_data:
            current = current.next
        if not current:
            print("El nodo previo no existe en la lista.")
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        """Elimina el primer nodo que contenga el valor especificado."""
        current = self.head
        previous = None

        while current and current.data != data:
            previous = current
            current = current.next

        if not current:
            print("Elemento no encontrado.")
            return

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def search(self, data):
        """Busca un valor en la lista y devuelve True si lo encuentra."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        """Muestra todos los elementos de la lista."""
        if self.is_empty():
            print("La lista está vacía.")
            return
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))
