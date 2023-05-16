from math import *

# 1
# 1.1
def raizDe2() -> float:
    return round(sqrt(2), ndigits=4)

# 1.2
def imprimir_hola():
    print("hola")

# 1.3
def imprimir_un_verso():
    verso = "Yerga el ande la cumbre más alta\nDe la mar el metal de su voz\nY entre nieves y cielos eternas\nSe alza el trono del libertador\n"
    print(verso)

# 1.4
def factorial_de_dos() -> int:
    f = 2*1
    return f

# 1.5
def factorial_3() -> int:
    f = 3 * factorial_de_dos()
    return f

# 1.6
def factorial_4() -> int:
    f = 4 * factorial_3()
    return f

# 1.7
def factorial_5() -> int:
    f = 5 * factorial_4()
    return f

# 2
# 2.1
def imprimir_saludo(nombre: str):
    print("Hola " + nombre)

# 2.2
def raiz_cuadrada_de(numero: float) -> float:
    res: float = sqrt(numero)
    return res

# 2.3
def imprimir_dos_veces(estribillo: str):
    print(estribillo * 2)

# 2.4
def es_multiplo_de(n: int, m: int) -> bool:
    res: bool = n % m == 0
    return res
    
# 2.5
def es_par(n: int) -> bool:
    res: bool = es_multiplo_de(n, 2)
    return res

# 2.6
def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    porciones_por_pizza: int = 8
    minima_cantidad_de_pizzas: int = ceil((comensales * min_cant_de_porciones) / porciones_por_pizza)
    return minima_cantidad_de_pizzas

# 3.
# 3.1
def alguno_es_0(numero1: int, numero2: int) -> bool:
    res: bool = numero1 == 0 or numero2 == 0
    return res

# 3.2
def ambos_son_0(numero1: int, numero2: int) -> bool:
    res: bool = numero1 == 0 or numero2 == 0
    return res

# 3.3
def es_nombre_largo(nombre: str) -> bool:
    longitud = len(nombre)
    res : bool = longitud >= 3 and longitud <= 8
    return res

# 3.4
def es_bisiesto(año: int) -> int:
    res: bool = es_multiplo_de(año, 400) or (es_multiplo_de(año, 4) and not es_multiplo_de(año, 100))
    return res

# 4.1
def peso_pino(altura: float) -> float:
    altura_en_cm: int = altura * 100
    peso: float = 3 * min(300, altura_en_cm) + 2 * max(0, altura_en_cm - 300)
    return peso

# 4.2
def es_peso_util(peso: float) -> bool:
    res: bool = (min(peso, 400) >= 400) and (max(peso, 1000) <= 1000)
    return res

# 4.3, 4.4
def sirve_pino(altura: float) -> bool:
    peso: float = peso_pino(altura)
    res: bool = es_peso_util(peso)
    return res

# 5.
# 5.1
def devolver_el_doble_si_es_par(un_numero: int) -> int:
    if es_par(un_numero):
        res: int = 2 * un_numero
    else: 
        res: int = un_numero 

    return res

# 5.2
def devolver_valor_si_es_par_sino_el_que_sigue_1(un_numero: int) -> int:
    if es_par(un_numero):
        res: int = un_numero
    
    if not (es_par(un_numero)):
        res: int = un_numero + 1

    return res

def devolver_valor_si_es_par_sino_el_que_sigue_2(un_numero: int) -> int:
    if es_par(un_numero):
        res: int = un_numero
    else:
        res: int = un_numero + 1

    return res

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9_1(n: int) -> int:
    if (n % 9 == 0):
        res: int = 3*n
    else:
        if (n % 3 == 0):
            res: int = 2*n
        else:
            res: int = n
    return res

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9_2(n: int) -> int:
    if (n % 3 == 0):
        res: int = 2*n
    if (n & 9 == 0):
        res: int = 3*n
    if ((n % 3 != 0) and (n % 9 != 0)):
        res: int = n

    return res

def nombre_tiene_muchas_letras(nombre: str) -> str:
    longitud: int = len(nombre)
    if longitud >= 5:
        res: str = "Tu nombre tiene muchas letras!"
    else: 
        res: str = "Tu nombre tiene menos de 5 letras"
    return res

# 5.5
def trabaja_o_vacaciona(sexo: str, edad: int) -> str:
    frase_trabajo = "Te toca trabajar"
    frase_vaciones = "Andá de vacaciones"
    if edad < 18: 
        res: str = frase_vaciones
    else:
        if sexo == "F":
            if edad < 60:
                res: str = frase_trabajo
            else:
                res: str = frase_vaciones
        if sexo == "M":
            if edad < 65:
                res: str = frase_trabajo
            else:
                res: str = frase_vaciones
    return res

# Especificaciones:
# problema devolver_el_doble_si_es_par(n: Z) : Z {
#   requiere: {True}
#   asegura: {(n 'mod' 2 = 0 --> res = 2*n ∧ (n 'mod' 2/= 0 --> res = n} (formal)
#            {si n es par, res es igual al doble de n y si n es impar, res es igual a n} (semiformal)
# }
# problema devolver_valor_si_es_par_sino_el_que_sigue_2(n: Z) : Z {
#   requiere: {True}
#   asegura: {(n 'mod' 2 = 0 --> res = n ∧ (n 'mod' 2 /= 0) --> res = n+1} (formal)
#            {si n es par, res es igual a n y si n es impar, res es igual a n+1} (semiformal)
# }
# problema devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9_1(n : Z) : Z {
#   requiere: {True}
#   asegura: {(n 'mod' 9 = 0 --> res = 3*n} si n es múltiplo de 9, res es 3*n
#   asegura: {(n 'mod' 3 = 0 --> res = 2*n} si n no es múltiplo de 9 y es múltiplo de 3, res es 2*n
#   asegura: {(n 'mod' 9 /= 0) ∧ (n 'mod' 3 /= 0) --> res = n} si n no es múltiplo de 3 ni de 9, res es n
# }
# problema nombre_tiene_muchas_letras(nombre: seq<Char>) : seq<Char> {
#   requiere: {|nombre| > 0}
#   asegura: {|nombre| >= 5 --> res = 'Tu nombre tiene muchas letras!' } 
#   asegura: {|nombre| < 5 --> res = 'Tu nombre tiene menos de 5 caracteres' }
# }
# problema trabaja_o_vacaciona(sexo: Char, edad: Z) : seq<Char> {
#   requiere: {edad >= 0}
#   requiere: {sexo = 'F' ∨ sexo = 'M'}
#   asegura: {si la edad es menor a 18, res es "Andá de vacaciones"}
#   asegura: {si el sexo es femenino y la edad es menor a 60, res es "Te toca trabajar"}
#   asegura: {si el sexo es femenino y la edad es mayor o igual a 65, res es "Andá a de vacaciones"}
#   asegura: {si el sexo es masculino y la edad es menor a 65, res es "Te toc trabajar"}
#   asegura: {si el sexo es masculino y la edad es mayor o igual a 65, res es "Andá a de vacaciones"}
# }

# 6.
# 6.2
def imprimir_pares_entre_10_y_40():
    i: int = 10
    while (i <= 40):
        if es_par(i):
            print(i)
        i += 1

