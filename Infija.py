class Pila:
    def __init__(self):
        self.items = []
    def push(self, valor):
        self.items.append(valor)
    def pop(self):
        return self.items.pop()
    def top(self):
        return self.items[-1] if self.items else None
    def vacia(self):
        return len(self.items) == 0


# --- Evaluación Postfija ---
def evaluar_postfija(expresion):
    pila = Pila()
    for token in expresion.split():
        if token.isdigit():
            pila.push(int(token))
        else:
            b = pila.pop()
            a = pila.pop()
            if token == '+': pila.push(a + b)
            elif token == '-': pila.push(a - b)
            elif token == '*': pila.push(a * b)
            elif token == '/': pila.push(a / b)
    return pila.pop()


# --- Evaluación Prefija ---
def evaluar_prefija(expresion):
    pila = Pila()
    tokens = expresion.split()[::-1]
    for token in tokens:
        if token.isdigit():
            pila.push(int(token))
        else:
            a = pila.pop()
            b = pila.pop()
            if token == '+': pila.push(a + b)
            elif token == '-': pila.push(a - b)
            elif token == '*': pila.push(a * b)
            elif token == '/': pila.push(a / b)
    return pila.pop()


# --- Conversión Infija → Postfija ---
def infija_a_postfija(expresion):
    precedencia = {'+':1, '-':1, '*':2, '/':2}
    pila = Pila()
    salida = []
    tokens = expresion.split()

    for token in tokens:
        if token.isdigit():
            salida.append(token)
        elif token in "+-*/":
            while (not pila.vacia() and pila.top() != '(' and
                   precedencia[pila.top()] >= precedencia[token]):
                salida.append(pila.pop())
            pila.push(token)
        elif token == '(':
            pila.push(token)
        elif token == ')':
            while not pila.vacia() and pila.top() != '(':
                salida.append(pila.pop())
            pila.pop()
    while not pila.vacia():
        salida.append(pila.pop())
    return " ".join(salida)


# --- Conversión Infija → Prefija ---
def infija_a_prefija(expresion):
    # Invertimos la expresión, convertimos a postfija y luego invertimos otra vez
    tokens = expresion.split()[::-1]
    for i in range(len(tokens)):
        if tokens[i] == '(':
            tokens[i] = ')'
        elif tokens[i] == ')':
            tokens[i] = '('
    invertida = " ".join(tokens)
    postfija = infija_a_postfija(invertida)
    prefija = postfija.split()[::-1]
    return " ".join(prefija)


# --- Programa principal ---
while True:
    print("\n=== Conversor y Evaluador de Expresiones ===")
    print("1. Ingresar expresión INFija")
    print("2. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        exp = input("Ingrese la expresión INFija (use espacios, ej: ( 3 + 4 ) * 2 ): ")

        print("\nConvertir a:")
        print("1. Postfija")
        print("2. Prefija")
        subop = input("Elige una opción: ")

        if subop == "1":
            post = infija_a_postfija(exp)
            print("Expresión en Postfija:", post)
            print("Resultado =", evaluar_postfija(post))
        elif subop == "2":
            pref = infija_a_prefija(exp)
            print("Expresión en Prefija:", pref)
            print("Resultado =", evaluar_prefija(pref))
        else:
            print("Opción no válida.")

    elif opcion == "2":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")
