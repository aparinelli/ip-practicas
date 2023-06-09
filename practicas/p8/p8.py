from random import *

vocales: list([str]) = ['a', 'e', 'i', 'o', 'u']

# 1.
# 1.1
def pertenece1(s: list([int]), e: int) -> bool:
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

# Para tipos genéricos
def pertenece(s, e) -> bool:
    res: bool = False
    for i in range(0, len(s)):
        if s[i] == e:
            res = True
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
    vocales: list([str]) = ['a', 'e', 'i', 'o', 'u']
    cant_vocales: int = 0
    res: bool = False

    for letra in palabra:
        if pertenece(vocales, letra):
            cant_vocales += 1
    
    if cant_vocales >= 3:
        res = True
    
    return res

# 2.
# 2.1
def colocar_ceros_en_pares_inout(lista: list([int])):
    for i in range(0, len(lista), 2):
        lista[i] = 0

# 2.2
def colocar_ceros_en_pares_in(lista: list([int])):
    res: list([int]) = lista.copy()
    for i in range(0, len(res), 2):
        res[i] = 0
    return res

# 2.3
def elimina_vocales(cadena: str):
    vocales: list([str]) = ['a', 'e', 'i', 'o', 'u']
    res: str = ""

    for letra in cadena:
        if not(pertenece(vocales, letra)):
            res += letra

    return res

# 2.4
def reemplaza_vocales(cadena: str):
    vocales: list([str]) = ['a', 'e', 'i', 'o', 'u']
    res: str = ""

    for letra in cadena:
        if pertenece(vocales, letra):
            res += ' '
        else: 
            res += letra

    return res

# 2.5
def da_vuelta_str(cadena: str):
    res: str = ""

    for i in range(len(cadena)-1, -1, -1):
        res += cadena[i]

    return res

# 3.
# 3.1
def construye_lista_de_nombres() -> list([str]):
    nombres: list([str]) = []
    
    while (True):
        nombre = input("Ingrese el nombre de un estudiante: ")
        if nombre == "listo":
            break
        nombres.append(nombre)
    
    return nombres

# 3.2
def construye_historial_de_monedero() -> list([(str, int)]):
    historial: list([(str, int)]) = []
    
    while (True):
        operacion = input("Ingrese C para cargar créditos, D para descontar créditos o X para terminar: ")
        if operacion == 'C':
            monto: int = int(input("Ingrese el monto a cargar: "))
            historial.append((operacion, monto))
        if operacion == 'D':
            monto: int = int(input("Ingrese el monto a descontar: "))
            historial.append((operacion, monto))
        if operacion == 'X':
            break
    
    return historial

# 3.3
def siete_y_medio() -> list([int]):
    cartas: list([int]) = [1,2,3,4,5,6,7,10,11,12]
    historial: list([int]) = []
    suma_total: float = 0

    while(True):
        continuar = input("¿Desea sacar una carta? (s)í o (n)o: ")
        
        if continuar == "n":
            break
        else:
            carta: int = choice(cartas)
            
            historial.append(carta)
            if pertenece([10,11,12], carta):
                suma_total += 0.5
            else:
                suma_total += carta
            
            if suma_total > 7.5:
                break
    
    print("¡Perdiste! Tus cartas fueron: ", historial)
    return historial

# 4
# 4.1 
def pertenece_a_cada_uno(s: list([[int]]), e: int) -> list([bool]):
    res: list([bool]) = []
    for i in range(0, len(s)):
        if pertenece(s[i], e):
            res.append(True)
        else:
            res.append(False)
    return res

# 4.2
def es_matriz(s: list([[int]])) -> bool:
    res: bool = True
    if len(s) != 0 and len(s[0]) != 0:
        longitud_de_primera_fila = len(s[0])
        for i in range(1, len(s)):
            if len(s[i]) != longitud_de_primera_fila:
                res = False
    else:
        res = False

    return res

# 4.3
def filas_ordenadas(m: list([[int]])) -> list([bool]):
    res: list([bool]) = []
    for i in range(0, len(m)):
        res.append(ordenados(m[i]))
    return res

# 4.4
import numpy as np
def elevar_matriz(d: int, p: int) -> np.array:
    matriz: np.array = np.random.random((d, d))
    res: np.array = matriz.copy()
    print("matriz: ")
    print(matriz)

    while p > 0:
        for i in range(d): # filas
            for j in range(d): # columnas
                suma: float = 0
                for n in range(0, d):
                    suma += res[i][n] * matriz[n][j]
                res[i][j] = suma
        p -= 1
    
    return res

