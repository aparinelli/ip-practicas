-- No editar esta parte
main :: IO ()
main = do
  x <- readLn
  print (sumaMenosQueMax (x :: (Int, Int, Int)))

sumaMenosQueMax :: (Int, Int, Int) -> Bool
sumaMenosQueMax (t0, t1, t2) = (maximo t0 t1 t2) > (minimo t0 t1 t2) + (medio t0 t1 t2)
-- Completar acá la definición de la función

-- Pueden agregan las funciones que consideren necesarias
maximo :: Int -> Int -> Int -> Int
maximo a b c | a >= b && a >= c = a
          | b >= a && b >= c = b
          | c >= a && c >= b = c

minimo :: Int -> Int -> Int -> Int
minimo a b c | a <= b && a <= c = a
          | b <= a && b <= c = b
          | c <= a && c <= b = c

medio :: Int -> Int -> Int -> Int
medio a b c | a >= b &&  a <= c || a <= b && a >= c = a
            | b >= a && b <= c || b <= a && b >= c = b
            | c >= a && c <= b || c <= a && c >= b = c