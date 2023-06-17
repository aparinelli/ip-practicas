from typing import List
from typing import Dict
import json

def unir_diccionarios(a_unir: List[Dict[str,str]]) -> Dict[str,List[str]]:
  # Implementar esta funcion
  
  unido: dict = {}

  for diccionario in a_unir:
    for clave in diccionario:
      valor_nuevo = diccionario[clave]
      if clave in unido.keys():
        unido[clave].append(valor_nuevo)
      else:
        unido[clave] = [valor_nuevo]

  return unido


if __name__ == '__main__':
  x = json.loads(input()) 
  
  # Tests:
  # [] --> {} Lista vacía
  # [{"a":2}] --> {"a": [2]} Un solo diccionario
  # [{"a":2}, {"b":1, "c":3}] --> {"a": [2], "b":[1], "c":[3]} Sin claves repetidas
  # [{"a":2},{"b":3,"a":1}] --> {'a': [2, 1], 'b': [3]} Una clave repetida
  # [{"a":2},{"b":3,"a":2}] --> {'a': [2,2], 'b': [3]} Una clave repetida con valores iguales
  # [{"a":2, "b": 4},{"b":3,"a":1}] --> {'a': [2, 1], 'b': [4,3]} Varias claves repetidas
  # [{}, {"a": 2}] --> {"a": 2} Un diccionario vacío
  # [{}, {}] --> {} Todos diccionarios vacíos

  print(unir_diccionarios(x))