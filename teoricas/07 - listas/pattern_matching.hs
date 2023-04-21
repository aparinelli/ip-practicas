longitud :: [a] -> Int
longitud [] = 0
longitud (_:xs) = 1 + longitud xs
-- en este caso, la lista tiene esta pinta: "algo : lista"
-- "xs" es x plural 

sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

pertenece :: (Eq a) => a -> [a] -> Bool
pertenece e [] = False
pertenece e (x:xs) = e == x || pertenece e xs

