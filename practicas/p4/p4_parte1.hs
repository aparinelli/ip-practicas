--1.
fibonacci :: Integer -> Integer
fibonacci n | n == 0 = 0
            | n == 1 = 1
            | n > 1 = fibonacci (n-1) + fibonacci (n-2)

--2.
parteEntera :: Float -> Integer
parteEntera n | n >= 0 && n < 1 = 0 
              | n > 0 = parteEntera (n-1) + 1
              | n < 0 = parteEntera (n+1) - 1


--3.
esDivisible :: Integer -> Integer -> Bool
esDivisible x y | x == y = True
                | y > x = False
                | otherwise = esDivisible (x - y) y

--4.
sumaImpares :: Integer -> Integer
sumaImpares n | n == 1 = 1
              | n > 1 = (n * 2 - 1) + sumaImpares(n - 1)


--5.
medioFact :: Integer -> Integer
medioFact n | n == 0 = 1
            | n == 1 = 1
            | otherwise = n * medioFact (n-2)

--6.
sumaDigitos :: Integer -> Integer
sumaDigitos n | n < 10 = n
              | otherwise = digitoUnidades n + sumaDigitos (div n 10)

--7.
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n < 10 = True
                      | otherwise = ultimosDosDigitosIguales && todosDigitosIguales (div n 10)
                      where ultimosDosDigitosIguales = (digitoUnidades n == digitoDecenas n)

digitoUnidades :: Integer -> Integer
digitoUnidades n = mod n 10

digitoDecenas :: Integer -> Integer
digitoDecenas n = digitoUnidades (div n 10)

--8.
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | i == (cantDigitos n) = digitoUnidades n
                 | otherwise = iesimoDigito (div n 10) i
    
cantDigitos :: Integer -> Integer
cantDigitos n | n < 10 = 1
              | otherwise = 1 + cantDigitos (div n 10)


--9.
esCapicua :: Integer -> Bool
esCapicua n | (cantDigitos n) == 1 = True
            | (cantDigitos n) == 2 || (cantDigitos n) == 3 = primerYUltimoCoinciden
            | (cantDigitos n) > 3 = primerYUltimoCoinciden && esCapicua (sinPrimerYUltimo n)
            where primerYUltimoCoinciden = (primerDigito n) == (ultimoDigito n)

-- requiere que n tenga tres o más cifras
sinPrimerYUltimo :: Integer -> Integer
sinPrimerYUltimo n = div (mod n (10^((cantDigitos n)- 1))) 10

primerDigito :: Integer -> Integer
primerDigito n = iesimoDigito n 1

ultimoDigito :: Integer -> Integer
ultimoDigito n = digitoUnidades n
 

--10. 
--a.
f1 :: Integer -> Integer
f1 n | n == 0 = 0
     | otherwise = 2^n + f1 (n-1)

--b.
f2 :: Integer -> Integer -> Integer
f2 n q | n == 0 = 0
       | otherwise = q^n + f2 (n-1) q

--c. 
f3 :: Integer -> Integer -> Integer
f3 n q = f2 (2*n) q

--d. 
f4 :: Integer -> Integer -> Integer
f4 n q = f2 (2*n) q - f2 (n-1) q

--11.
eAprox :: Integer -> Float
eAprox n | n == 0 = 1 / fromInteger (factorial 0)
         | otherwise = 1 / fromInteger (factorial n) + eAprox (n-1)

factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n-1)

--12.
raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = (sucesion n) - 1

sucesion :: Integer -> Float
sucesion n | n == 1 = 2
           | otherwise = 2 + 1 / (sucesion (n-1))

--13.
sumatoriaDoble :: Integer -> Integer -> Integer
sumatoriaDoble 0 _ = 0 
sumatoriaDoble n m = sumatoriaDoble (n-1) m + sumatoriaInterna n m

sumatoriaInterna :: Integer -> Integer -> Integer
sumatoriaInterna _ 0 = 0
sumatoriaInterna n j = n^j + sumatoriaInterna n (j-1)

--14. 
sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias _ 0 _ = 0
sumaPotencias q n m = sumaPotencias q (n-1) m + sumaPotenciasInterna q n m

sumaPotenciasInterna :: Integer -> Integer -> Integer -> Integer
sumaPotenciasInterna _ _ 0 = 0
sumaPotenciasInterna q n m = q^(n+m) + sumaPotenciasInterna q n (m-1)

--15.
sumaRacionales :: Integer -> Integer -> Float
sumaRacionales 0 _ = 0
sumaRacionales n m = sumaRacionales (n-1) m + sumaRacionalesInterna n m

sumaRacionalesInterna :: Integer -> Integer -> Float
sumaRacionalesInterna _ 0 = 0
sumaRacionalesInterna p q = (fromInteger p)/(fromInteger q) + sumaRacionalesInterna p (q-1)

--16. 
--a.
menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorDesde n 2

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n m | mod n m == 0 = m
                      | otherwise = menorDivisorDesde n (m+1)

--b.
esPrimo :: Integer -> Bool
esPrimo n | menorDivisor n == n = True
          | otherwise =  False

--c.
sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos a b | menorDivisor a == menorDivisor b = False
                | ambosPrimos && a /= b = True
                | otherwise = sonCoprimos (menorDivisor a) cocienteB && sonCoprimos cocienteA (menorDivisor b)
                where ambosPrimos = esPrimo a && esPrimo b
                      cocienteA = div a (menorDivisor a)
                      cocienteB = div b (menorDivisor b)
--d.
nEsimoPrimo :: Integer -> Integer
nEsimoPrimo n = nEsimoPrimoAux 2 2 0 n

nEsimoPrimoAux :: Integer -> Integer -> Integer -> Integer -> Integer
nEsimoPrimoAux primoAnterior p primosContados n
 | primosContados == n = primoAnterior
 | esPrimo p = nEsimoPrimoAux p (p+1) (primosContados+1) n
 | not (esPrimo p) = nEsimoPrimoAux primoAnterior (p+1) primosContados n

--17.
esFibonacci :: Integer -> Bool
esFibonacci n = esFibonacciAux n 0 0

esFibonacciAux :: Integer -> Integer -> Integer -> Bool
esFibonacciAux n i fibAnterior 
 | fibAnterior == n = True
 | fibAnterior > n = False
 | fibAnterior < n = esFibonacciAux n (i+1) (fibonacci (i+1))

--18.
mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n | esPar ultimo = elMayor ultimo (mayorDigitoPar restoDelNumero) 
                 | ultimo == restoDelNumero = -1
                 | otherwise = mayorDigitoPar restoDelNumero
                 where
                     ultimo = mod n 10
                     restoDelNumero = div n 10

elMayor :: Integer -> Integer -> Integer
elMayor x y | x >= y = x
            | x < y = y

esPar :: Integer -> Bool
esPar n = mod n 2 == 0

--19.
esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos n = esSIPAux n 1 2

esSIPAux :: Integer -> Integer -> Integer -> Bool
esSIPAux n i sumaAnterior 
 | sumaAnterior == n = True
 | sumaAnterior > n = False
 | sumaAnterior < n = esSIPAux n (i+1) (sumaMPrimos (i+1))

sumaMPrimos :: Integer -> Integer
sumaMPrimos m | m == 1 = 2
              | otherwise = nEsimoPrimo m + sumaMPrimos (m-1)

--20.
tomaValorMax :: Integer -> Integer -> Integer
tomaValorMax n1 n2 = tomaValorMaxAux n1 n2 n1 (sumaDivisores n1)

tomaValorMaxAux :: Integer -> Integer -> Integer -> Integer -> Integer
tomaValorMaxAux i n2 m sumaAnterior
 | i == n2+1 = m
 | sumaDivisores i >= sumaAnterior = tomaValorMaxAux (i+1) n2 i (sumaDivisores i)
 | otherwise = tomaValorMaxAux (i+1) n2 m sumaAnterior

sumaDivisores :: Integer -> Integer
sumaDivisores n = sumaDivisoresHasta n n

sumaDivisoresHasta :: Integer -> Integer -> Integer
sumaDivisoresHasta n 1 = 1
sumaDivisoresHasta n i 
 | mod n i == 0 = i + sumaDivisoresHasta n (i-1)
 | otherwise = sumaDivisoresHasta n (i-1)