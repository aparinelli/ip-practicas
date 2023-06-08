from pilas import *

print("2. Pilas")

print("\n2.8")
print('generar_nros_al_azar(10, 1, 100)')
print(generar_nros_al_azar(10, 1, 100))
print('generar_nros_al_azar(20, 1, 50)')
print(generar_nros_al_azar(20, 1, 50))

print("\n2.9")
print('pila_aleatoria()')
print(pila_aleatoria().queue)

print("\n2.10")
p = pila_aleatoria()
print("Pila original: ", p.queue)
print('cantidad_de_elementos(p)')
print(cantidad_de_elementos(p))
print("No modifiqué la pila original: ", p.queue)

print("\n2.11")
p = pila_aleatoria()
print("Pila original: ", p.queue)
print('buscar_el_maximo(p)')
print(buscar_el_maximo(p))
print("No modifiqué la pila original: ", p.queue) # 

print("2.12")
print(esta_bien_balanceada("1 + (2 * 3 - (20 / 5))"))
print(esta_bien_balanceada("10 * (1 + (2 * (-1)))"))
print(esta_bien_balanceada("(1)"))
print(esta_bien_balanceada("()"))
print(esta_bien_balanceada("10 * (1 + (* 2 * (-1)))"))
print(esta_bien_balanceada("10 * (1 + (2 * (-1))))"))