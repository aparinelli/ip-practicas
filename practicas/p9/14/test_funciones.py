import pytest
from funciones import existe_elemento

def test_existe_elemento_1():
    s = [1,2]
    e = 2
    assert existe_elemento(s, e) == True

def test_existe_elemento_2():
    s = [1,1]
    e = 2
    assert existe_elemento(s, e) == False