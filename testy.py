import pytest
from moduły_gry import *

@pytest.fixture
def e():
    return Engine()
def test_zwieksz_bulls(e):
    e.staty.zwieksz_bulls()
    assert e.staty.bulls==1
def test_zwieksz_cows(e):
    e.staty.zwieksz_cows()
    assert e.staty.cows==1
@pytest.mark.parametrize("bull,cow",[(5,6),(1,2),(8,0)])
def test_resetowanie_stat(e,bull,cow):
    e.staty.bulls=bull
    e.staty.cows=cow
    e.staty.resetowanie_stat()
    assert e.staty.bulls==0 and e.staty.cows==0
@pytest.mark.parametrize("string,boolean",[("nos",True),("kawa",False),("skarpeta",False),("kapelusz",True)])
def test_validator(e,string,boolean):
    assert e.izogram.jest_izogramem(string)==boolean
@pytest.mark.parametrize("słowo,bulls,wynik",[("nos",3,True),("kapelusz",5,False)])
def test_sprawdzanie_zgadywania(e,słowo,bulls,wynik):
    e.staty.bulls=bulls
    e.sprawdzanie_zgadywania(słowo)
    assert  e.sprawdzanie_zgadywania(słowo)==wynik
@pytest.mark.parametrize("bulls,cows,twojes,s",[(4,0,"mysz","mysz"),(1,0,"dom","kot"),(0,2,"dupa","apel")])
def test_sprawdzanie_slowa(e,bulls,cows,twojes,s):
    e.sprawdzanie_slowa(twojes,s)
    assert e.staty.bulls==bulls and e.staty.cows==cows


