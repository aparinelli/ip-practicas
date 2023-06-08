# 1. Archivos
# 1.1
# 1.1.1
def contarlineas(nombre_archivo: str) -> int:
    archivo = open(nombre_archivo, "r")
    lineas: list([str]) = archivo.readlines()
    archivo.close()

    cantidad_de_lineas: int = len(lineas)

    return cantidad_de_lineas

# 1.1.2
def existe_palabra(palabra_buscada: str, nombre_archivo: str) -> bool:
    archivo = open(nombre_archivo, "r")
    texto: str = archivo.read()
    archivo.close()

    res: bool = False
    
    palabra_actual: str = ""

    for caracter in texto:
        if es_separador(caracter):
            if palabra_actual == palabra_buscada:
                res = True
            else:
                palabra_actual = ""
        else:
            palabra_actual += caracter
    
    if palabra_actual == palabra_buscada:
        res = True

    return res

def es_separador(caracter: str) -> bool:
    return caracter in [' ', '.', ',', '¿', '?', '¡', '!','\n']

# 1.1.3
def cantidad_de_apariciones(nombre_archivo: str, palabra_buscada: str) -> int:
    archivo = open(nombre_archivo, "r")
    texto: str = archivo.read().lower()
    archivo.close()

    res: int = 0

    palabra_actual: str = ""

    for caracter in texto:
        if es_separador(caracter):
            if palabra_actual == palabra_buscada:
                res += 1
            else:
                palabra_actual = ""
        else:
            palabra_actual += caracter

    if palabra_actual == palabra_buscada:
        res += 1

    return res

# 1.2
def clonar_sin_comentarios(nombre_archivo: str): 
    archivo_existente = open(nombre_archivo, "r")
    lineas: list([str]) = archivo_existente.readlines()
    archivo_existente.close()
    
    archivo_sin_comentarios = open("clonado.txt", "w")
    lineas_sin_comentar = []
    for linea in lineas:
        es_comentario: bool = True
        
        hay_espacios_antes_del_comentario: bool = True
        i: int = 0
        while (i < len(linea) and linea[i] != "#"):
            if linea[i] != " ":
                hay_espacios_antes_del_comentario = False
            i += 1

        if not hay_espacios_antes_del_comentario:
            es_comentario = False
        
        if not es_comentario:
            lineas_sin_comentar.append(linea)
    
    archivo_sin_comentarios.writelines(lineas_sin_comentar)

# 1.3
def generar_reverso(nombre_archivo: str):
    archivo_existente = open(nombre_archivo, "r")
    lineas: list([str]) = archivo_existente.readlines()
    archivo_existente.close()

    lineas_invertidas: list([str]) = lineas [::-1]
    lineas_invertidas[0] += '\n' # la última línea del archivo existente no tenía el '\n' 
    lineas_invertidas[-1] = lineas_invertidas[-1][:-1] # elimino el último '\n' de la última línea

    archivo_reverso = open("reverso.txt", "w")
    archivo_reverso.writelines(lineas_invertidas)

# 1.4
def agregar_frase_al_final(nombre_archivo: str, frase: str):
    archivo = open(nombre_archivo, "a")
    archivo.write(frase)
    archivo.close()

# 1.5
def agregar_frase_al_principio(nombre_archivo: str, frase: str):
    archivo = open(nombre_archivo, "r")
    contenido = archivo.read()
    archivo.close()

    contenido = frase + contenido

    archivo = open(nombre_archivo, "w")
    archivo.write(contenido)
    archivo.close()

# 1.6
def leer_en_binario(nombre_archivo: str) -> list([str]):
    archivo = open(nombre_archivo ,"rb")
    contenido = archivo.read()
    archivo.close()
    palabras_legibles: list([str]) = []
    palabra_legible: str = ""

    for byte in contenido:
        if es_caracter_legible(byte):
            palabra_legible += chr(byte)
        else:
            if len(palabra_legible) >= 5:
                palabras_legibles.append(palabra_legible)
            palabra_legible = ""
    
    if len(palabra_legible) >= 5: # Agrego la última palabra legible
        palabras_legibles.append(palabra_legible)
    
    return palabras_legibles

def es_caracter_legible(b: hex) -> bool:
    caracter = chr(b)
    return caracter in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz _"

# 1.7
def promedio_estudiante(LU: str) -> float:
    archivo = open("notas.csv")
    lineas: list([str]) = archivo.readlines()
    archivo.close()

    cantidad_de_notas: int = 0
    suma_de_notas: int = 0
    for linea in lineas:
        LU_materia_fecha_nota: list = linea.split(',')
        if LU_materia_fecha_nota[0] == LU:
            cantidad_de_notas += 1
            suma_de_notas += float(LU_materia_fecha_nota[-1])

    promedio: float = suma_de_notas / cantidad_de_notas

    return promedio