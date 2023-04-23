-- No editar esta parte
main :: IO()
main = do {
  x <- readLn ;
  print(prod(x ::(Integer)))
  }

-- Completar la definición de la función
prod :: Integer -> Integer
prod n = prodBase (2*n)

-- Pueden agregan las funciones que consideren necesarias
prodBase :: Integer -> Integer
prodBase n | n == 0 = 1
           | otherwise = (n^2 + 2*n) * prodBase (n-1)