# 4
# 4.18

def agrupar_por_longitud(nombre_archivo: str) -> dict:
    archivo = open(nombre_archivo, "r")
    texto = archivo.read()
    archivo.close()

    palabras = texto.split(" ")

    longitudes_agrupadas = {}
    for palabra in palabras: 
        longitud: int = len(palabra)

        if longitud in longitudes_agrupadas:
            longitudes_agrupadas[longitud] += 1
        else:
            longitudes_agrupadas[longitud] = 1
    
    return longitudes_agrupadas

