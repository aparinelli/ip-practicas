from queue import Queue as Cola
import random

def generar_nros_al_azar(n: int, desde: int, hasta: int) -> list([int]):
    return random.sample(range(desde, hasta+1), k=n)

def cola_aleatoria():
    c = Cola()
    nros_al_azar: list([int]) = generar_nros_al_azar(8, 1, 50)
    for n in nros_al_azar:
        c.put(n)
    return c


