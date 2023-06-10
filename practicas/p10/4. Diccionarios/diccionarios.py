# 4
# 4.18

def agrupar_por_longitud(nombre_archivo: str) -> dict:
    archivo = open(nombre_archivo, "r")
    texto: str = archivo.read()
    archivo.close()

    palabras: list([str]) = texto.split(" ")

    longitudes_agrupadas: dict = {}
    for palabra in palabras: 
        longitud: int = len(palabra)
        if longitud in longitudes_agrupadas:
            longitudes_agrupadas[longitud] += 1
        else:
            longitudes_agrupadas[longitud] = 1
    
    return longitudes_agrupadas

# 4.19
def armar_diccionario_de_promedios() -> dict:
    archivo = open("notas.csv")
    lineas = archivo.readlines()
    archivo.close()

    notas: dict = {}

    for linea in lineas:
        LU_materia_fecha_nota: list = linea.split(',')
        LU: str = LU_materia_fecha_nota[0]
        nota: int = int(LU_materia_fecha_nota[-1])
        
        if LU in notas:
            notas[LU].append(nota)
        else:
            notas[LU] = [nota]
    
    promedios = {}

    for LU in notas.keys():
        cantidad_de_notas: int = len(notas[LU])
        suma_de_notas: int = 0
        for nota in notas[LU]:
            suma_de_notas += nota
        
        promedio: float = suma_de_notas / cantidad_de_notas

        promedios[LU] = promedio
    
    return promedios
        
# 4.20
def la_palabra_mas_frecuente(nombre_archivo: str) -> str:
    archivo = open(nombre_archivo)
    lineas = archivo.readlines()
    archivo.close()

    apariciones = {}

    for linea in lineas:
        palabras = linea.split()
        for palabra in palabras:
            if palabra in apariciones:
                apariciones[palabra] += 1
            else:
                apariciones[palabra] = 1
    
    maximo: int = 0
    palabra_mas_frecuente: str = ""
    for palabra in apariciones.keys():
        if apariciones[palabra] >= maximo:
            maximo = apariciones[palabra]
            palabra_mas_frecuente = palabra
        
    return palabra_mas_frecuente