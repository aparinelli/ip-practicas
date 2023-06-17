from queue import LifoQueue

def calcular_expresion(expr: str):
    
    operadores_y_operandos: list[str] = expr.split()
    pila: LifoQueue = LifoQueue()

    for i in range(len(operadores_y_operandos)):
        e: str = operadores_y_operandos[i]
        if '.' in e or e.isalnum():
            pila.put(float(e))
        elif e == '+':
            n2 = pila.get()
            n1 = pila.get()
            pila.put(n1 + n2)
        elif e == '*':
            n2 = pila.get()
            n1 = pila.get()
            pila.put(n1 * n2)
        elif e == '-':
            n2 = pila.get()
            n1 = pila.get()
            pila.put(n1 - n2)
        elif e == '/':
            n2 = pila.get()
            n1 = pila.get()
            pila.put(n1 / n2)
    
    res = pila.get()
    return res

if __name__ == '__main__':
    expr: str = input()
    print(calcular_expresion(expr))