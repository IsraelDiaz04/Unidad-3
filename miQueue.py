from miNode import Node

class Queue:
    def __init__(self):
        self.top = None   # primer nodo
        self.last = None  # último nodo
        self.count = 0

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def front(self):
        if self.is_empty():
            return None
        return self.top.info

    def enqueue(self, info):
        new_node = Node(info)
        if self.is_empty():
            self.top = self.last = new_node
        else:
            self.last.set_next(new_node)
            self.last = new_node
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            return None
        info = self.top.info
        self.top = self.top.get_next()
        self.count -= 1
        if self.is_empty():
            self.last = None
        return info

    def print_info(self):
        print(f"\nQueue size: {self.size()}")
        node = self.top
        while node is not None:
            node.info.print()
            node = node.get_next()

    def get_nth(self, pos):
        if pos < 1 or pos > self.count:
            return None
        node = self.top
        for _ in range(1, pos):
            node = node.get_next()
        return node.info
