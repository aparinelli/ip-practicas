import sys

def quienGana(j1: str, j2: str) -> str : 
    #Implementar esta funcion
    puntajes: list([(str, str, str)]) = [
       ("Piedra", "Piedra", "Empate"),
       ("Piedra", "Tijera", "Jugador1"),
       ("Piedra", "Papel", "Jugador2"),
       ("Papel", "Papel", "Empate"),
       ("Papel", "Piedra", "Jugador1"),
       ("Papel", "Tijera", "Jugador2"),
       ("Tijera", "Tijera", "Empate"),
       ("Tijera", "Papel", "Jugador1"),
       ("Tijera", "Piedra", "Jugador2")
    ]

    res: str = ""

    for puntaje in puntajes:
       if puntaje[0] == j1 and puntaje[1] == j2:
          res = puntaje[2]
    
    return res

if __name__ == '__main__':
  x = input()
  jug = str.split(x)
  print(quienGana(jug[0], jug[1]))