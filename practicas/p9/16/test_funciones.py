import pytest
from funciones import es_subsecuencia, iguales

def test_es_subsecuencia_1():
    s = [1,2,3]
    r = [2,3]
    assert es_subsecuencia(s, r) == True

def test_es_subsecuencia_2():
    s = [1,2]
    r = [3]
    assert es_subsecuencia(s, r) == False

def test_iguales():
    s = [1,2,3]
    r = [1,2]
    assert iguales(s, r) == False