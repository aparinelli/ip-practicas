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
sacarBlancosRepetidos s = sacarBlancosRepetidosAux (limpiarExtremos s)

sacarBlancosRepetidosAux :: [Char] -> [Char]
sacarBlancosRepetidosAux s
 | not (pertenece ' ' s) = s
 | head s == ' ' && segundo s == ' ' =  sacarBlancosRepetidosAux (tail s)
 | otherwise = (head s) : sacarBlancosRepetidosAux (tail s)

limpiarExtremos :: [Char] -> [Char]
-- elimina todos los blancos del principio y del final de la lista
limpiarExtremos s
 | ultimo s /= ' ' && head s /= ' ' = s
 | head s == ' ' = limpiarExtremos (tail s)
 | ultimo s == ' ' = limpiarExtremos (principio s)

--4.2
contarPalabras :: [Char] -> Integer
contarPalabras s = contarPalabrasAux (limpiarExtremos (sacarBlancosRepetidos s))

contarPalabrasAux :: [Char] -> Integer
contarPalabrasAux s
 | not (pertenece ' ' s) = 1
 | head s == ' ' = 1 + contarPalabrasAux (tail s)
 | otherwise = contarPalabrasAux (tail s)

--4.3
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga s = palabraMasLargaAux (sacarBlancosRepetidos (limpiarExtremos s))

palabraMasLargaAux :: [Char] -> [Char]
palabraMasLargaAux [] = []
palabraMasLargaAux s
 | contarPalabras s == 1 = s
 | otherwise = masLargaEntreDos (primPalabra s) (palabraMasLargaAux (quitarPrimPalabra s))

primPalabra :: [Char] -> [Char]
primPalabra [] = []
primPalabra (x:xs)
 | x == ' ' = []
 | otherwise = x : primPalabra xs

quitarPrimPalabra :: [Char] -> [Char]
quitarPrimPalabra [] = []
quitarPrimPalabra s
 | head s == ' ' = tail s
 | otherwise = quitarPrimPalabra (tail s)

masLargaEntreDos :: [Char] -> [Char] -> [Char] 
masLargaEntreDos s r
 | longitud s >= longitud r = s
 | longitud s < longitud r = r

--4.4
palabras :: [Char] -> [[Char]]
palabras s = palabrasAux (sacarBlancosRepetidos (limpiarExtremos s))

palabrasAux :: [Char] -> [[Char]]
palabrasAux [] = []
palabrasAux s
 | contarPalabras s == 1 = [s]
 | otherwise = primPalabra s : palabrasAux (quitarPrimPalabra s)

--4.5
aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (x:xs) = x ++ aplanar (xs)

--4.6
aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos s
 | longitud s == 1 = head s
 | otherwise = head s ++ " " ++ aplanar (tail s)

--4.7
aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
aplanarConNBlancos [] _ = []
aplanarConNBlancos s n
 | longitud s == 1 = head s
 | otherwise = head s ++ (nBlancos n) ++ aplanar (tail s)

nBlancos :: Integer -> [Char]
nBlancos 1 = " "
nBlancos n = " " ++ nBlancos (n-1)

--5.
--5.1
nat2bin :: Integer -> [Integer]
nat2bin 0 = [0]
nat2bin 1 = [1]
nat2bin n = (nat2bin (div n 2)) ++ [mod n 2]

--5.2
bin2nat :: [Integer] -> Integer
bin2nat [0] = 0
bin2nat [1] = 2
bin2nat (x:xs) = 2^((longitud (x:xs)) - 1) * x + bin2nat xs

--5.3
nat2hex :: Integer -> [Char]
nat2hex n
 | n < 16 = [iesimo n digitosHex]
 | otherwise = nat2hex (div n 16) ++ [iesimo (mod n 16) digitosHex]
 where digitosHex = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

iesimo :: Integer -> [t] -> t
iesimo i s
 | i == (longitud s) - 1 = ultimo s
 | otherwise = iesimo i (principio s) 

--5.4
sumaAcumulada :: [Integer] -> [Integer]
sumaAcumulada [] = []
sumaAcumulada [x] = [x]
sumaAcumulada s = sumaAcumulada (principio s) ++ [sumatoria s]

--5.5
descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos [x] = [descomponerEnPrimosUnico x]
descomponerEnPrimos (x:xs) = (descomponerEnPrimosUnico x) : (descomponerEnPrimos xs)

descomponerEnPrimosUnico :: Integer -> [Integer]
descomponerEnPrimosUnico n
 | esPrimo n = [n]
 | otherwise = eliminarRepetidos ((menorDivisor n) : (descomponerEnPrimosUnico multiplicador))
 where multiplicador = div n (menorDivisor n)

menorDivisor :: Integer -> Integer
menorDivisor 1 = 1
menorDivisor n = menorDivisorDesde n 2

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n m | mod n m == 0 = m
                      | otherwise = menorDivisorDesde n (m+1)

esPrimo :: Integer -> Bool
esPrimo n | menorDivisor n == n = True
          | otherwise =  False

--6.
--6.1