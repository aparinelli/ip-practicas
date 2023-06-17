-- No editar esta parte
main :: IO()
main = do {
  x <- readLn ;
  print(combinacionesMenoresOiguales(x ::(Integer)))
  }

combinacionesMenoresOiguales :: Integer -> Integer
combinacionesMenoresOiguales n = sumatoriaExterna n n n
-- Completar la definición de la función

sumatoriaExterna :: Integer -> Integer -> Integer -> Integer
sumatoriaExterna n i j | i == 0 = 0
                       | otherwise = sumatoriaExterna n (i-1) j + sumatoriaInterna n i j

sumatoriaInterna :: Integer -> Integer -> Integer -> Integer
sumatoriaInterna n i j | j == 0 = 0
                       | i * j <= n = 1 + sumatoriaInterna n i (j-1)
                       | otherwise = sumatoriaInterna n i (j-1)
-- Pueden agregan las funciones que consideren necesarias


