# Recursión sobre listas

```
[1,2,1] :: [Int]
[True, False, True] :: [Int]
[]
```
* se pueden repetir elementos
* todos los elementos son del mismo tipo
 
## Operaciones

```
head :: [a] -> a      
tail :: [a] -> [a]      
(:) :: a -> [a] -> [a] 
```
* `head` devuelve el primer elemento
* `tail` devuelve la lista sin el primer elemento
* `(:)` agrega el elemento indicado al principio de la lista. 

### Ejemplos
`head [1,2,3] : [4, 5]` > `[1,4,5]`

`head ([1,2,3] : [4,5])` > **error**, porque `[1,2,3] : [4,5]` no se puede hacer: `[1,2,3]` tiene tipo `[Int]` y para poder hacer `(:)`,  `[4,5]` debería tener tipo `[[Int]]`

## Recursión

```
ver recursion_sobre_listas.hs
```

## Pattern matching

```
ver pattern_matching.hs
```

## Conjuntos

```
ver conjuntos.hs
```
