-- 1.
--a.
f :: Integer -> Integer
f n | n == 1 = 8
    | n == 4 = 131
    | n == 16 = 16

--b.
g :: Integer -> Integer
g n | n == 8 = 16
    | n == 16 = 4
    | n == 131 = 1

--c.
h :: Integer -> Integer
h n = f (g n)

--d.
k :: Integer -> Integer
k n = g (f n)

--2.
--a.
absoluto :: Integer -> Integer
absoluto n | n < 0 = -n
           | n >= 0 = n

--b.
maximo :: Integer -> Integer -> Integer
maximo x y | x >= y = x
           | otherwise = y

maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto x y = maximo (absoluto x) (absoluto y)

--c.
maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z = maximo (maximo x y) z

--d.
algunoEs0 :: Float -> Float -> Bool
-- Con pattern matching:

-- algunoEs0 0 y = True
-- algunoEs0 x 0 = True
-- algunoEs0 x y = False

-- Sin pattern matching:

algunoEs0 x y = (x == 0) || (y == 0)

--e.
ambosSon0 :: Float -> Float -> Bool

-- Con pattern matching:

-- ambosSon0 0 0 = True
-- ambosSon0 a b = False

-- Sin pattern matching:

ambosSon0 x y = (x == 0) && (x == y)

--f.
mismoIntegerervalo :: Float -> Float -> Bool
mismoIntegerervalo x y | x <= 3 && y <= 3 = True
                   | x > 3 && x <= 7 && y > 3 && y <= 7 = True
                   | x > 7 && y > 7 = True
                   | otherwise = False

--g. 
sumaDistIntegeros :: Integer -> Integer -> Integer -> Integer
sumaDistIntegeros a b c | a == b && b == c = a
                    | a /= b && a == c = a + b
                    | a /= b && b == c = a + b
                    | a /= c && a == b = a + c
                    | b /= c && a == c = b + c
                    | a /= b && a /= c = a + b + c

--h.
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe a b = mod a b == 0

--i.
digitoUnidades :: Integer -> Integer
digitoUnidades n = mod n 10

--j.
digitoDecenas :: Integer -> Integer
digitoDecenas n = digitoUnidades (div n 10)

--3.
estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b = (mod a b) == 0
-- res = true <=> a * a + a * b * k = 0  donde a, b, k son números enteros distintos de 0
--            <=> a * (a + b * k) = 0
--            <=> a + b * k = 0
--            <=> k = -a / b
--            <=> mod a b = 0            (para que k sea un número entero)

--4.
--a.
prodInt :: (Float, Float) -> (Float, Float) -> Float
prodInt (a0, a1) (b0, b1) = a0 * b0 + a1 * b1

--b.
todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor (a0, a1) (b0, b1) = (a0 < b0) && (a1 < b1)

--c.
distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos (x1, y1) (x2, y2) = sqrt ((x2 - x1)**2 + (y2 - y1)**2)

--d.
sumaTerna :: (Float, Float, Float) -> Float
sumaTerna (a0, a1, a2) = a0 + a1 + a2

--e.
esMultiplo :: 

sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (a0, a1, a2) n  | ((mod a0 n) == 0) && ((mod a1 n) == 0) && ((mod a2 n) == 0) = a0 + a1 + a2
                                  | ((mod a0 n) == 0) && ((mod a1 n) == 0) && ((mod a2 n) /= 0) = a0 + a1
                                  | ((mod a0 n) == 0) && ((mod a1 n) /= 0) && ((mod a2 n) == 0) = a0 + a2
                                  | ((mod a0 n) /= 0) && ((mod a1 n) == 0) && ((mod a2 n) == 0) = a1 + a2
                                  | ((mod a0 n) == 0) && ((mod a1 n) /= 0) && ((mod a2 n) /= 0) = a0
                                  | ((mod a0 n) /= 0) && ((mod a1 n) == 0) && ((mod a2 n) /= 0) = a1
                                  | ((mod a0 n) /= 0) && ((mod a1 n) /= 0) && ((mod a2 n) == 0) = a2
                                  | otherwise = 4

--f.
posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (a0, a1, a2) | (mod a0 2) == 0 = 0
                          | ((mod a0 2) /= 0) && ((mod a1 2) == 0) = 1
                          | ((mod a0 2) /= 0) && ((mod a1 2) /= 0) && ((mod a2 2) == 0) = 2
                          | otherwise = 4

--g.
crearPar :: t1 -> t2 -> (t1, t2)
crearPar a0 a1 = (a0, a1)

--h.
invertir :: (t1, t2) -> (t2, t1)
invertir (a0, a1) = (a1, a0)