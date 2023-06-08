from queue import LifoQueue
import random

# 2. Pilas

# 2.8
def generar_nros_al_azar(n: int, desde: int, hasta: int) -> list([int]):
    return random.sample(range(desde, hasta+1), k=n)

# 2.9
def pila_aleatoria() -> LifoQueue:
    nros_al_azar: list([int]) = generar_nros_al_azar(5, 1, 50)
    
    pila = LifoQueue()
    for n in nros_al_azar:
        pila.put(n)
    return pila


# 2.10
def cantidad_de_elementos(p: LifoQueue) -> int:
    cantidad: int = 0
    nueva_pila: LifoQueue = copiar_pila(p)

    while not nueva_pila.empty():
        _ = nueva_pila.get()
        cantidad += 1
        
    return cantidad

# 2.11
def buscar_el_maximo(p: LifoQueue) -> int:
    nueva_pila: LifoQueue = copiar_pila(p)

    if not nueva_pila.empty():
        maximo: int = nueva_pila.get()
        while not nueva_pila.empty():
            ultimo: int = nueva_pila.get()
            if  ultimo > maximo:
                maximo = ultimo
        return maximo 

# 2.12
def esta_bien_balanceada(s: str) -> bool:
    p = LifoQueue()

    for simbolo in s[::-1]:
        if simbolo != " ":
            p.put(simbolo)
    
    bien_balanceada: bool = True
    parentesis: int = 0
    
    anteriores = LifoQueue()
    anteriores.put('(')

    while not p.empty():
        simbolo: str = p.get()
        simbolo_anterior: str = anteriores.get()
        if simbolo == '(':
            if es_operacion(simbolo_anterior) or simbolo_anterior == '(': # solo permito operaciones y '(' antes de ')'
                parentesis += 1
            else:
                bien_balanceada = False
            anteriores.put(simbolo)

        elif simbolo == ')':
            if es_numero(simbolo_anterior) or simbolo_anterior == ')': # solo permito números y paréntesis antes de ')'
                parentesis -= 1
            else:
                bien_balanceada = False
            anteriores.put(simbolo)

        else:
            if es_operacion(simbolo):
                if es_operacion(simbolo_anterior):
                    bien_balanceada = False
                if simbolo_anterior == '(':
                    if simbolo != '-': # solo permito numeros negativos
                        bien_balanceada = False
            elif es_numero(simbolo):
                if simbolo_anterior == ')':
                    bien_balanceada = False

            anteriores.put(simbolo)
         
        if parentesis < 0:
            bien_balanceada = False
        
    return bien_balanceada

def es_numero(simbolo: str) -> bool:
    return simbolo in "0123456789"

def es_operacion(simbolo: str) -> bool:
    return simbolo in "+-*/"

# Auxiliares
def copiar_pila(p: LifoQueue) -> LifoQueue:
    lista_intermedia = []

    while not p.empty():
        lista_intermedia.append(p.get())
    
    nueva_p = LifoQueue()

    for i in range(len(lista_intermedia) - 1, -1, -1):
        p.put(lista_intermedia[i])
        nueva_p.put(lista_intermedia[i])
    
    return nueva_p

