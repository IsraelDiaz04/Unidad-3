import tkinter as tk
from tkinter import simpledialog, messagebox

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def mostrar(self):
        return self.items.copy()

# Funciones para los botones
def apilar():
    elemento = simpledialog.askstring("Apilar", "Ingresa el elemento a apilar:")
    if elemento is not None:
        pila.apilar(elemento)
        actualizar_lista()
        messagebox.showinfo("✓ Apilado", f"Elemento '{elemento}' apilado.")

def desapilar():
    elemento = pila.desapilar()
    if elemento is not None:
        actualizar_lista()
        messagebox.showinfo("✗ Desapilado", f"Elemento '{elemento}' desapilado.")
    else:
        messagebox.showwarning("Pila vacía", "No hay elementos para desapilar.")

def ver_cima():
    elemento = pila.cima()
    if elemento is not None:
        messagebox.showinfo("Cima de la pila", f"Elemento en cima: {elemento}")
    else:
        messagebox.showwarning("Pila vacía", "La pila está vacía.")

def actualizar_lista():
    lista.delete(0, tk.END)
    for i, item in enumerate(reversed(pila.mostrar()), start=1):
        lista.insert(tk.END, f"{i}: {item}")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Pila - Interfaz Gráfica")
ventana.geometry("300x400")

pila = Pila()

tk.Button(ventana, text="Apilar", width=15, command=apilar).pack(pady=5)
tk.Button(ventana, text="Desapilar", width=15, command=desapilar).pack(pady=5)
tk.Button(ventana, text="Ver Cima", width=15, command=ver_cima).pack(pady=5)
tk.Button(ventana, text="Salir", width=15, command=ventana.destroy).pack(pady=5)

# Lista para mostrar la pila
lista = tk.Listbox(ventana, width=30, height=15)
lista.pack(pady=10)

ventana.mainloop()
