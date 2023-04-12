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
           | n > 0 = n
           | otherwise = 0

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
mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo x y | x <= 3 && y <= 3 = True
                   | x > 3 && x <= 7 && y > 3 && y <= 7 = True
                   | x > 7 && y > 7 = True
                   | otherwise = False


