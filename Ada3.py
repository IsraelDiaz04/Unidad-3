from bisect import bisect_left

# ---------------- FUNCIONES AUXILIARES ---------------- #

def normalize(name: str) -> str:
    return name.strip().lower()

def find_index(postres, name):
    """Devuelve el índice del postre (o -1 si no existe)."""
    nrm = normalize(name)
    for i, p in enumerate(postres):
        if normalize(p['name']) == nrm:
            return i
    return -1

def insert_postre(postres, name, ingredients):
    """Da de alta un postre manteniendo el orden alfabético."""
    if not name.strip():
        print("⚠️ El nombre del postre no puede estar vacío.")
        return False

    keys = [normalize(p['name']) for p in postres]
    pos = bisect_left(keys, normalize(name))

    if pos < len(postres) and normalize(postres[pos]['name']) == normalize(name):
        print(f"⚠️ El postre '{name}' ya existe, se combinarán ingredientes.")
        for ing in ingredients:
            if ing not in postres[pos]['ingredients']:
                postres[pos]['ingredients'].append(ing)
        return False
    else:
        postres.insert(pos, {'name': name.strip(), 'ingredients': ingredients})
        print(f"✅ Postre '{name}' agregado correctamente.")
        return True

def print_ingredients(postres, name):
    idx = find_index(postres, name)
    if idx == -1:
        print(f"❌ El postre '{name}' no existe.")
    else:
        print(f"\nIngredientes de '{postres[idx]['name']}':")
        for ing in postres[idx]['ingredients']:
            print(f"  - {ing}")

def add_ingredient(postres, name, ingredient):
    idx = find_index(postres, name)
    if idx == -1:
        print(f"❌ El postre '{name}' no existe.")
        return
    if ingredient in postres[idx]['ingredients']:
        print(f"⚠️ El ingrediente '{ingredient}' ya está en la lista.")
        return
    postres[idx]['ingredients'].append(ingredient)
    print(f"✅ Ingrediente '{ingredient}' agregado a '{name}'.")

def remove_ingredient(postres, name, ingredient):
    idx = find_index(postres, name)
    if idx == -1:
        print(f"❌ El postre '{name}' no existe.")
        return
    if ingredient not in postres[idx]['ingredients']:
        print(f"⚠️ El ingrediente '{ingredient}' no se encuentra en '{name}'.")
        return
    postres[idx]['ingredients'].remove(ingredient)
    print(f"✅ Ingrediente '{ingredient}' eliminado de '{name}'.")

def delete_postre(postres, name):
    idx = find_index(postres, name)
    if idx == -1:
        print(f"❌ El postre '{name}' no existe.")
        return
    del postres[idx]
    print(f"✅ Postre '{name}' eliminado completamente.")

def remove_duplicates(postres):
    """Elimina postres repetidos combinando sus ingredientes."""
    seen = {}
    to_delete = []
    for i, p in enumerate(postres):
        key = normalize(p['name'])
        if key in seen:
            existing = postres[seen[key]]['ingredients']
            for ing in p['ingredients']:
                if ing not in existing:
                    existing.append(ing)
            to_delete.append(i)
        else:
            seen[key] = i
    for i in sorted(to_delete, reverse=True):
        del postres[i]
    print(f"✅ {len(to_delete)} postre(s) duplicado(s) eliminado(s).")

def mostrar_postres(postres):
    print("\n🍮 LISTA DE POSTRES:")
    if not postres:
        print("(vacía)")
    for p in postres:
        print(f" - {p['name']}: {', '.join(p['ingredients'])}")

# ---------------- PROGRAMA PRINCIPAL ---------------- #

def main():
    POSTRES = []

    while True:
        print("\n" + "="*40)
        print(" MENÚ DE POSTRES ".center(40, "="))
        print("1. Dar de alta un postre con ingredientes")
        print("2. Mostrar ingredientes de un postre")
        print("3. Agregar ingrediente a un postre")
        print("4. Eliminar ingrediente de un postre")
        print("5. Dar de baja un postre")
        print("6. Eliminar postres duplicados")
        print("7. Mostrar todos los postres")
        print("0. Salir")
        print("="*40)

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre del postre: ").strip()
            ingredientes = []
            print("Ingresa los ingredientes (escribe 'fin' para terminar):")
            while True:
                ing = input("Ingrediente: ").strip()
                if normalize(ing) == "fin":
                    break
                if ing and ing not in ingredientes:
                    ingredientes.append(ing)
            insert_postre(POSTRES, nombre, ingredientes)

        elif opcion == "2":
            nombre = input("Nombre del postre: ")
            print_ingredients(POSTRES, nombre)

        elif opcion == "3":
            nombre = input("Nombre del postre: ")
            ing = input("Ingrediente a agregar: ")
            add_ingredient(POSTRES, nombre, ing)

        elif opcion == "4":
            nombre = input("Nombre del postre: ")
            ing = input("Ingrediente a eliminar: ")
            remove_ingredient(POSTRES, nombre, ing)

        elif opcion == "5":
            nombre = input("Nombre del postre a eliminar: ")
            delete_postre(POSTRES, nombre)

        elif opcion == "6":
            remove_duplicates(POSTRES)

        elif opcion == "7":
            mostrar_postres(POSTRES)

        elif opcion == "0":
            print("👋 Programa finalizado.")
            break

        else:
            print("❌ Opción no válida. Intenta nuevamente.")

# ----------------------------------------------------- #
if __name__ == "__main__":
    main()
