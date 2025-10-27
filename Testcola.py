from miQueue import Queue
from miOrder import Order

def main():
    queue = Queue()

    # Crear pedidos
    o1 = Order(10, "Cliente A")
    o2 = Order(5, "Cliente B")
    o3 = Order(8, "Cliente C")
    o4 = Order(12, "Cliente D")

    # Agregar pedidos
    queue.enqueue(o1)
    queue.print_info()

    queue.enqueue(o2)
    queue.print_info()

    queue.enqueue(o3)
    queue.print_info()

    queue.enqueue(o4)
    queue.print_info()

    # Ver el primer pedido sin eliminarlo
    print("\nFront element:")
    front_order = queue.front()
    if front_order:
        front_order.print()

    # Eliminar el primer pedido
    print("\nDequeue (remove front element):")
    removed_order = queue.dequeue()
    if removed_order:
        removed_order.print()
    queue.print_info()

    # Obtener el 3er elemento
    print("\n3rd element in queue:")
    nth_order = queue.get_nth(3)
    if nth_order:
        nth_order.print()
    else:
        print("Invalid position")

if __name__ == "__main__":
    main()