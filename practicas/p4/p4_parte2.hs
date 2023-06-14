--21.
pitagoras :: Integer -> Integer -> Integer -> Integer
pitagoras m n r = contarPares m n r 0 0 

contarPares :: Integer -> Integer -> Integer -> Integer -> Integer -> Integer
contarPares m n r p q
 | p > m = 0
 | q > n = contarPares m n r (p+1) 0 
 | p^2 + q^2 <= r^2 = 1 + contarPares m n r p (q+1) 
 | otherwise = contarPares m n r p (q+1) 