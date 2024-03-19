

# Moduly a importy

import math
from math import pi as moje_krasna_konstanta


# print(math.pi)
# print(moje_krasna_konstanta)

import statistics

# print(statistics.mean([1,2,2,2,3]))

# Kde vezmu dalsi moduly?
# mohu najit v dokumentaci nebo vygoogli
# mohu si vytvorit vlastni soubor ktery se bude chovat jako modul
# doinstaluju - budeme si ukazovat pozdeji v kurzu

# print(round(0.5))
# print(math.ceil(2.01))
# print(math.floor(3.99))

# Funkce
# Pouzivame abychom si zjednodusili kod - nemusime opakovat stejne radky nekolikrat s jinou hodnotou
# Muzeme si kousky kodu pojmenovat - oznacit, abychom vedeli my (nebo i ostatni) k cemu je pouzit


# tato funkce vypisuje, zatim nepouziva return
# Nema zadny parametr
def greet_user():
    # kod co ta funkce dela
    print("Ahoj!")

# Toto je muj soubor ktery se nachazi ve stejne slozce jako tento skript
# (v jine slozce nebude tento zapis fungovat)
from vlastni_modul import greet_user

# scope / rozsah / kontext = misto kde je dana promenna platna

name = 'Andrea'

def greet_user_v2(name):
    # tato funkce pouziva return, vraci tedy nejakou hodnotu
    # zadny print zde neni, nic tedy sama o osbe nevypisuje
    if name == 'Andrea':
        return 'Cau!'
    else:
        return f"Ahoj {name}!"

name = 'Jitko'
vysledek = greet_user_v2(name)
print(vysledek)


# Nepovinne parametry + ruzne zpusoby volani funkce s jejimi parametry - 1 otazka v kvizu

# Oba parametry povinne
def mult(a, b):
    return a * b

print(mult(2, 3))
print(mult(a=2, b=3))
print(mult(b=2, a=3))
print(mult(2, b=3))

# Nefunguje protoze positional musi byt pred keyword parametrem
# print(mult(a=2, 3))

def mult_tri_hodnoty(a, b=5, c=10):
    return a * b * c

print(mult_tri_hodnoty(2))
print(mult_tri_hodnoty(a=10, b=10, c=100))



# Typovani - pouze zminka o tom abyste vedeli ze existuje - 1 otazka v kvizu
# Oba parametry povinne, pozor ze python vas stejne necha zadat i jiny datovy typ ktery muze zpusobit neocekavane vysledky
def mult(a: int, b: int=10) -> int:
    ','.join([])
    return a * b

print(mult('3', 10))

# V kombinaci s assert nize byste mohli neocekavane chovani zachytit
# assert mult(3, 10) == 30, "Vysledek by mel byt tricet"
# assert mult('3', 10) == 30, "Vysledek by mel byt tricet ikdyz treba zadam str misto int"

# Assert - 1 otazka v kvizu

def mult_rozbita(a, b):
    return a * b+1

def mult(a, b):
    return a * b

vysledek = mult(10, 10)
assert vysledek == 100, "Funkce by mela pouze vynasobit dve cisla, vtomto pripade 10 * 10"

# vysledek = mult_rozbita(10, 10)
# assert vysledek == 100, "Funkce by mela pouze vynasobit dve cisla, vtomto pripade 10 * 10"

print('Vse v poradku')
