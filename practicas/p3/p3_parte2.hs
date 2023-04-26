--5.
todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (n1, n2, n3) = ((f n1) > (g n1)) && ((f n2) > (g n2)) && ((f n3) > (g n3))

f :: Integer -> Integer
f n | n <= 7 = n^2
    | n > 7 = 2*n - 1

g :: Integer -> Integer
g n | (mod n 2) == 0 = div n 2
    | otherwise = 3 * n + 1

--- todosMenores (4, 6, 10) = True
--- todosMenores (3, 6, 10) = False

--6.
bisiesto :: Integer -> Bool
bisiesto año | (esMultiplo año 4) && not (esMultiplo año 100) = True
             | (esMultiplo año 100) && (esMultiplo año 400) = True
             | otherwise = False

esMultiplo :: Integer -> Integer -> Bool
esMultiplo x y = (mod x y) == 0

--7.
distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan p q = sumatoriaTerna p q 2

sumatoriaTerna :: (Float, Float, Float) -> (Float, Float, Float) -> Integer -> Float
sumatoriaTerna p q n 
 | n == 0 = distanciaAbsoluta (n_esimo p 0) (n_esimo q 0)
 | n > 0 = distanciaAbsoluta (n_esimo p n) (n_esimo q n) + (sumatoriaTerna p q (n-1))

distanciaAbsoluta :: Float -> Float -> Float
distanciaAbsoluta pi qi = abs (pi - qi)

n_esimo :: (t, t, t) -> Integer -> t
n_esimo (a0, a1, a2) 0 = a0
n_esimo (a0, a1, a2) 1 = a1
n_esimo (a0, a1, a2) 2 = a2

--8. 
comparar :: Integer -> Integer -> Integer
comparar a b | (sumaUltimosDosDigitos a) < (sumaUltimosDosDigitos b) = 1
             | (sumaUltimosDosDigitos a) > (sumaUltimosDosDigitos b) = -1
             | otherwise = 0

sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x = (mod x 10) + (mod (div x 10) 10)
