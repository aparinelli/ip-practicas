from queue import Queue
from typing import List
from typing import Dict
from typing import Union
import json

# ACLARACIÓN: El tipo de "pedidos" debería ser: pedidos: Queue[Dict[str, Union[int, str, Dict[str, int]]]]
# Por no ser soportado por la versión de CMS, usamos simplemente "pedidos: Queue"
def procesamiento_pedidos(pedidos: Queue,
                          stock_productos: Dict[str, int],
                          precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
  
  res = []

  while not pedidos.empty():
    pedido: dict = pedidos.get()
    
    # Recibo información del pedido
    id_cliente = pedido["id"]
    nombre_cliente = pedido["cliente"]
    productos: dict = pedido["productos"]

    # Proceso los productos solicitados
    productos_procesados: dict = {}
    precio_total: float = 0
    estado: str = "completo"
    for nombre in productos:
      cantidad_solicitada: int = productos[nombre]
      stock: int = stock_productos[nombre]
      
      cantidad_procesada = cantidad_solicitada
      if stock - cantidad_solicitada < 0:
        cantidad_procesada = stock
      
      if cantidad_procesada < cantidad_solicitada:
        estado = "incompleto"

      productos_procesados[nombre] = cantidad_procesada
      stock_productos[nombre] = stock - cantidad_procesada

      precio: float = precios_productos[nombre]
      precio_total += precio * cantidad_procesada
    
    # Armo el pedido procesado
    pedido_procesado: dict = {}
    pedido_procesado["id"] = id_cliente
    pedido_procesado["cliente"] = nombre_cliente
    pedido_procesado["productos"] = productos_procesados
    pedido_procesado["precio_total"] = precio_total
    pedido_procesado["estado"] = estado

    res.append(pedido_procesado)

  return res


if __name__ == '__main__':
  pedidos: Queue = Queue()
  list_pedidos = json.loads(input())
  [pedidos.put(p) for p in list_pedidos]
  stock_productos = json.loads(input())
  precios_productos = json.loads(input())
  print("{} {}".format(procesamiento_pedidos(pedidos, stock_productos, precios_productos), stock_productos))

# Ejemplo input  
# pedidos: [{"id":21,"cliente":"Gabriela", "productos":{"Manzana":2}}, {"id":1,"cliente":"Juan","productos":{"Manzana":2,"Pan":4,"Factura":6}}]
# stock_productos: {"Manzana":10, "Leche":5, "Pan":3, "Factura":0}
# precios_productos: {"Manzana":3.5, "Leche":5.5, "Pan":3.5, "Factura":5}