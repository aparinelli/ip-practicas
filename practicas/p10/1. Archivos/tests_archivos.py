from archivos import *

print("\n1. Archivos")

print("\n1.1.1")
print('contarlineas("1.1.1.txt")')
print(contarlineas("1.1.1.txt"))

print("\n1.1.2")
print('existe_palabra("muchas", "1.1.1.txt")')
print(existe_palabra("muchas", "1.1.1.txt"))
print(existe_palabra("veces", "1.1.1.txt"))

print("\n1.1.3")
print('cantidad_de_apariciones("1.1.1.txt", "lineas")')
print(cantidad_de_apariciones("1.1.1.txt", "lineas"))

print("\n1.2: Descomentar línea correspondiente")
# clonar_sin_comentarios("1.2.txt")

print("\n1.3: Descomentar línea correspondiente")
# generar_reverso("1.3.txt")

print("\n1.4: Descomentar línea correspondiente")
# agregar_frase_al_final("1.4.txt", "\nUna frase al final")

print("\n1.5: Descomentar línea correspondiente")
# agregar_frase_al_principio("1.5.txt", "Una frase al principio\n")

print("\n1.6")
print('leer_en_binario("documento.pdf")')
print(leer_en_binario("documento.pdf"))
print('leer_en_binario("libro.epub")')
print(leer_en_binario("libro.epub"))

print("\n1.7")
print('promedio_estudiante("4931/20")')
print(promedio_estudiante("4931/20"))
