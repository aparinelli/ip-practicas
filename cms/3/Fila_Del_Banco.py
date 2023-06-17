from queue import Queue

# El tipo de fila debería ser Queue[int], pero la versión de python del CMS no lo soporta. Usaremos en su lugar simplemente "Queue"
def avanzarFila(fila: Queue, min: int):
  #implementar función
  
  ultimo_llegado = {"min": -4, "n": fila.qsize()}
  caja_1 = -9 # porque empieza en min 1
  caja_2 = -1 # porque empieza en min 3
  caja_3 = -2 # porque empieza en min 2
  ultimo_atendido_en_caja_3 = {"min": 0, "n": 0} # (minuto, numero_persona)

  for minuto in range(min+1):
    if minuto - ultimo_llegado["min"] == 4:
      nuevo_n = ultimo_llegado["n"] + 1

      fila.put(nuevo_n)
      ultimo_llegado["min"] = minuto
      ultimo_llegado["n"] = nuevo_n
    
    if minuto - ultimo_atendido_en_caja_3["min"] == 3:
      fila.put(ultimo_atendido_en_caja_3["n"])
    
    if minuto - caja_1 == 10:
      caja_1 = minuto
      if not fila.empty():
        fila.get()
    if minuto - caja_2 == 4:
      caja_2 = minuto
      if not fila.empty():
        fila.get()
    if minuto - caja_3 == 4:
      caja_3 = minuto
      if not fila.empty():
        n = fila.get()
        ultimo_atendido_en_caja_3["min"] = minuto
        ultimo_atendido_en_caja_3["n"] = n
      

if __name__ == '__main__':
  fila: Queue = Queue()
  fila_inicial: int = int(input())
  for numero in range(1, fila_inicial+1):
    fila.put(numero)
  min: int = int(input())
  avanzarFila(fila, min)
  res = []
  for i in range(0, fila.qsize()):
    res.append(fila.get())
  print(res)


# Caja1: Empieza a atender 10:01, y atiende a una persona cada 10 minutos
# Caja2: Empieza a atender 10:03, atiende a una persona cada 4 minutos
# Caja3: Empieza a atender 10:02, y atiende una persona cada 4 minutos, pero no le resuelve el problema y la persona debe volver a la fila (se va al final y tarda 3 min en llegar. Es decir, la persona que fue atendida 10:02 vuelve a entrar a la fila a las 10:05)
# La fila empieza con las n personas que llegaron antes de que abra el banco. Cuando abre (a las 10), cada 4 minutos llega una nueva persona a la fila (la primera entra a las 10:00)

# n = 5
# [1,2,3,4,5]
# 0: [1,2,3,4,5,6]
# 1: [2,3,4,5,6]
# 2: [3,4,5,6] -- 2 va a volver
# 3: [4,5,6] 
# 4: [4,5,6,7]
# 5: [4,5,6,7,2]
# 6: [5,6,7,2] -- 4 va a volver
# 7: [6,7,2]
# 8: [6,7,2,8]
# 9: [6,7,2,8,4]
# 10: [7,2,8,4] -- 6 va a volver
# 11: [8,4]


# caja 1 : atiende 1, 11, 21, 31
# caja 3: atiende 2, 6, 10, 14
# caja 2 : atiende 3, 7, 11, 15
# llega nuevo: 0, 4, 8, 12, 16, 20