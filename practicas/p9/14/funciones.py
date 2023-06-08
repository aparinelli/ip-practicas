def existe_elemento(s: list([int]), e: int) -> bool:
    result: bool = False
    for i in range(len(s)):
        if s[i] == e:
            result = True
            break
    return result