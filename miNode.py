class Node:
    def __init__(self, info):
        self.info = info
        self.next = None  # referencia al siguiente nodo

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node
