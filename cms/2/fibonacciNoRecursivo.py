import sys

def fibonacciNoRecursivo(n: int) -> int:
  # Implementar esta funcion
  res: int = 0
  if n == 0:
    res = 0
  if n == 1:
    res = 1
  if n > 1:
    i = 1
    suma = 0
    anteriores_dos = [0,1]
    while (i < n):
      suma = anteriores_dos[0] + anteriores_dos[1]
      anteriores_dos[0] = anteriores_dos[1]
      anteriores_dos[1] = suma
      i += 1
    res = suma
  return res

if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))