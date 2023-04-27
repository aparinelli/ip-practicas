--1.
--1.1 
longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

--1.2
ultimo :: [t] -> t
ultimo s | longitud s == 1 = head s
         | otherwise = ultimo (tail s)

--1.3
principio :: [t] -> [t]
principio s | longitud s == 1 = []
            | otherwise = (head s) : principio (tail s)

--1.4
reverso :: [t] -> [t]
reverso [] = []
reverso s = (ultimo s) : (reverso (principio s))

--2.
--2.1.
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece e [] = False
pertenece e (x:xs) = e == x || pertenece e xs

--2.2
todosIguales :: (Eq t) => [t] -> Bool
todosIguales s
 | longitud s == 1 = True
 | longitud s == 2 = (head s) == segundo
 | otherwise = (head s) == segundo && todosIguales (tail s)
 where segundo = head (tail s)

segundo :: [t] -> t
segundo s = head (tail s)

--2.3
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos s
 | longitud s == 1 = True
 | pertenece (head s) (tail s) = False
 | otherwise = todosDistintos (tail s)

--2.4
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos s = not (todosDistintos s)

--2.5 
quitar :: (Eq t) => t -> [t] -> [t]
quitar x s
 | not (pertenece x s) = s
 | x == (head s) = tail s
 | otherwise = (head s) : quitar x (tail s)

-- 2.6.
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos x s
 | not (pertenece x s) = s
 | x == (head s) = quitarTodos x (tail s)
 | otherwise = (head s) : quitarTodos x (tail s)

--2.7
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos s
 | not (hayRepetidos s) = s
 | pertenece (head s) (tail s) = eliminarRepetidos (tail s)
 | otherwise = (head s) : (eliminarRepetidos (tail s))

--2.8
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos s r
 | longitud s == 0 = False
 | longitud s == 1 = pertenece (head s) r
 | otherwise = pertenece (head s) r && mismosElementos (tail s) r 

--2.9
capicua :: (Eq t) => [t] -> Bool
capicua s = s == reverso s

--3.
--3.1
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

--3.2
productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x * productoria xs

--3.3
maximo :: [Integer] -> Integer
maximo s | longitud s == 1 = head s
         | longitud s == 2 = maximoEntreDos (head s) (segundo s)
         | otherwise = maximoEntreDos (head s) (maximo (tail s))

maximoEntreDos :: Integer -> Integer -> Integer
maximoEntreDos a b | a >= b = a
                   | a < b = b

--3.4
sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n s
 | longitud s == 1 = [(head s) + 1]
 | otherwise = ((head s) + n) : sumarN n (tail s)

--3.5
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero s = sumarN (head s) s

--3.6
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo s = sumarN (ultimo s) s

--3.7
pares :: [Integer] -> [Integer]
pares [] = []
pares s 
 | esPar (head s) = (head s) : pares (tail s) 
 | otherwise = pares (tail s)        
 
esPar :: Integer -> Bool
esPar a = mod a 2 == 0

--3.8
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n s
 | esMultiplo (head s) n = (head s) : multiplosDeN n (tail s)
 | otherwise = multiplosDeN n (tail s) 

esMultiplo :: Integer -> Integer -> Bool
esMultiplo a b = mod a b == 0

--3.9
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar s | longitud s == 1 = s
          | otherwise = ordenar (quitar (maximo s) s) ++ [maximo s]

--4.
--4.1.
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos s = sacarBlancosRepetidosAux (limpiarPrincipioYFinal s)

sacarBlancosRepetidosAux :: [Char] -> [Char]
sacarBlancosRepetidosAux s
 | not (pertenece ' ' s) = s
 | head s == ' ' && segundo s == ' ' =  sacarBlancosRepetidosAux (tail s)
 | otherwise = (head s) : sacarBlancosRepetidosAux (tail s)

limpiarPrincipioYFinal :: [Char] -> [Char]
-- elimina todos los blancos del principio y del final de la lista
limpiarPrincipioYFinal s
 | ultimo s /= ' ' && head s /= ' ' = s
 | head s == ' ' = limpiarPrincipioYFinal (tail s)
 | ultimo s == ' ' = limpiarPrincipioYFinal (principio s)

--4.2
contarPalabras :: [Char] -> Integer
contarPalabras s = contarPalabrasAux (limpiarPrincipioYFinal (sacarBlancosRepetidos s))

contarPalabrasAux :: [Char] -> Integer
contarPalabrasAux s
 | not (pertenece ' ' s) = 1
 | head s == ' ' = 1 + contarPalabrasAux (tail s)
 | otherwise = contarPalabrasAux (tail s)

-- [2,1] -> [1,2]
-- [2,3,1] -> [1,2,3]
-- []