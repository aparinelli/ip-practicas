def es_subsecuencia(s: list([int]), r: list([int])) -> list([int]):
    result: bool = False
    ultimoIndice: int = len(s) - len(r)
    for i in range(ultimoIndice + 1):
        subseq: list([int]) = subsecuencia(s, i, len(r))
        sonIguales: bool = iguales(subseq, r)
        if sonIguales:
            result = True
            break
    return result

def subsecuencia(s: list([int]), desde: int, longitud: int) -> list([int]):
    rv: list([int]) = []
    hasta: int = desde + longitud
    for i in range(desde, hasta):
        elem = s[i]
        rv.append(elem)
    return rv 

def iguales(a: list([int]), b: list([int])) -> bool:
    result: bool = True
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] != b[i]:
                result = False
                break
    else:
        result = False
    return result