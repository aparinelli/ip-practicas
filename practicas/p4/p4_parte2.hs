--21.
pitagoras :: Integer -> Integer -> Integer -> Integer
pitagoras m n r = sumatoriaDoble m n r

sumatoriaDoble :: Integer -> Integer -> Integer -> Integer
sumatoriaDoble 0 _ _ = 0
sumatoriaDoble p q r = sumatoriaDoble (p-1) q r + sumatoriaInterna p q r

sumatoriaInterna :: Integer -> Integer -> Integer -> Integer
sumatoriaInterna _ 0 _ = 0
sumatoriaInterna p q r 
 | p^2 + q^2 <= r^2 = 1 + sumatoriaInterna p (q-1) r
 | otherwise = sumatoriaInterna p q r


