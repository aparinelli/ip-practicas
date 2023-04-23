-- No editar esta parte
main :: IO()
main = do {
  x <- readLn ;
  print(sumaPrimerosNImpares(x ::(Integer)))
  }

sumaPrimerosNImpares :: Integer -> Integer
sumaPrimerosNImpares n = sumatoriaBase (2*n-1)
-- Completar la definición de la función

sumatoriaBase :: Integer -> Integer
sumatoriaBase n | n == 0 = 0
                | mod n 2 == 0 = 0 + sumatoriaBase (n-1)
                | mod n 2 /= 0 = (2*n + 2) + sumatoriaBase (n-1)
-- Pueden agregan las funciones que consideren necesarias

-- n = 2  ==>  2*1 +2 + 2*3 + 2 = 


