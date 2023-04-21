type Set a = [a]

vacio :: Set Int
vacio = []

pertenece :: Int -> [Int] -> Bool
pertenece e [] = False
pertenece e l |(head l) == e = True
              | otherwise = pertenece e (tail l)

agregar :: Int -> [Int] -> [Int]
agregar x [] = [x]
agregar x c | pertenece x c = c
            | otherwise = (x:c)
-- asegura: sinRepetidos(res) = True porque requerí sinRepetidos(c)
-- asegura: todos los elementos de s pertenecen a res y x pertenece a res
-- asegura: todos los elementos de res viene de x o de c

incluido :: [Int] -> [Int] -> Bool
incluido [] _ = True
incluido (x:xs) c = pertenece x c && incluido xs c

iguales :: [Int] -> [Int] -> Bool
iguales c1 c2 = incluido c1 c2 && incluido c2 c1