# 1.
# 1.1
def pertenece(s: list([int]), e: int) -> bool:
    res: bool = False
    for i in range(0, len(s)):
        if s[i] == e:
            res = True
    return res

def pertenece2(s: list([int]), e: int) -> bool:
    res: bool = False
    i: int = 0
    while (i < len(s)):
        if s[i] == e: 
            res = True
        i += 1
    return res

def pertenece3(s: list([int]), e: int) -> bool:
    res: bool = False
    for i in range(0, len(s)):
        res = s[i] == e or res
    return res

# 1.2
def divide_a_todos(s: list([int]), e: int) -> bool:
    res: bool = True
    for i in range(0, len(s)): 
        if s[i] % e != 0:
            res = False
    return res

# 1.3
def sumaTotal(s: list([int])) -> int:
    res: int = 0
    for i in range(0, len(s)):
        res += s[i]
    return res

# 1.4
def ordenados(s: list([int])) -> bool:
    res: bool = True
    for i in range(1, len(s)):
        if s[i] <= s[i-1]:
            res = False
    return res

# 1.5
def alguna_mas_larga_que_7(s: list([str])) -> bool:
    res: bool = False
    for i in range(0, len(s)):
        if len(s[i]) > 7: 
            res = True
    return res

# 1.6
def es_palindroma(s: str) -> bool:
    res: bool = True
    for i in range(0, len(s)):
        if s[i] != s[len(s)-i-1]:
            res = False
    return res

# 1.7
def es_contraseña_segura(contraseña: str) -> str:
    cant_de_minsuculas: int = 0
    cant_de_mayusculas: int = 0
    cant_de_numeros: int = 0
    
    for letra in contraseña: 
        if (letra >= 'a' and letra <= 'z'):
            cant_de_minsuculas += 1
        if (letra >= 'A' and letra <= 'Z'):
            cant_de_mayusculas += 1
        if (letra >= '0' and letra <= '9'):
            cant_de_numeros += 1
    
    res: str = "AMARILLA"
    if len(contraseña) > 8 and cant_de_minsuculas >= 1 and cant_de_mayusculas >= 1 and cant_de_numeros >= 1:
        res = "VERDE"
    else:
        if len(contraseña) < 5:
            res = "ROJA"
    return res

# 1.8
def saldo_actual(historial: list((str, int))) -> int:
    saldo: int = 0

    for movimiento in historial:
        if movimiento[0] == 'I':
            saldo += movimiento[1]
        if movimiento[0] == 'R':
            saldo -= movimiento[1]
    
    return saldo

# 1.9
def tiene_3_vocales_distintas(palabra: str):
    vocales: list([str]) = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    cant_vocales: int = 0
    res: bool = False

    for letra in palabra:
        if letra in vocales:
            cant_vocales += 1
    
    if cant_vocales >= 3:
        res = True
    
    return res