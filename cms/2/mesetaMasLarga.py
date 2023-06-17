from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def mesetaMasLarga(l: List[int]) -> int :
  # Implementar esta funcion
  mayor_meseta: int = 1
  meseta: int = 1
  if len(l) == 1:
    mayor_meseta = 1
  else: 
    anterior: int = l[0]
    for i in range(1, len(l)):
      if l[i] == anterior:
        meseta += 1
      else:
        if meseta > mayor_meseta:
          mayor_meseta = meseta
        meseta = 1
      anterior = l[i]

    if meseta > mayor_meseta:
      mayor_meseta = meseta

  return mayor_meseta

if __name__ == '__main__':
  x = input()
  print(mesetaMasLarga([int(j) for j in x.split()]))