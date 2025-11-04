from MyLinkedList.my_linked_list import MyLinkedList

lista = MyLinkedList()

lista.insert_at_end(10)
lista.insert_at_end(20)
lista.insert_at_beginning(5)
lista.insert_after(10, 15)

lista.display()

lista.delete(20)
lista.display()

print("¿Está 15 en la lista?", lista.search(15))
print("¿Está 100 en la lista?", lista.search(100))
