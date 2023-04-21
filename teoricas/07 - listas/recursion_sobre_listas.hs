longitud :: [a] -> Int  -- ahora es un polimorfismo
longitud [] = 0
longitud l = 1 + longitud (tail l)

suma :: Num a => [a] -> a
suma [] = 0
suma l = (head l) + suma (tail l)

pertenece :: Int -> [Int] -> Bool
pertenece e [] = False
pertenece e l |(head l) == e = True
              | otherwise = pertenece e (tail l)
