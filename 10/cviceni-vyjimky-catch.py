# https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/vyjimky/osetreni-vstupu

# 1 Ošetření dělení nulou
# Vytvoř program, který vypíše výsledek dělení těchto čísel.
# Program se postupně zeptá na dvě čísla (mohou být celá i desetinná).
# Vyděl tato čísla mezi sebou a vypiš výsledek dělení. Ošetři, aby program nezhavaroval při pokusu o dělení nulou.
# V tomto případě nemusíš ošetřovat zadání nečíselného vstupu, ošetření více výjimek v jednom bloku si ukážeme v další části.

a_str = input("Zadej prvni cislo: ")
b_str = input("Zadej druhe cislo: ")

# Osetrim a pak provedu

if not a_str.isdigit() or not b_str.isdigit():
    print("Zadejte prosim cislo")
    exit()

a = int(a_str)
b = int(b_str)

if b == 0:
    print("Nulou nelze delit")
    exit()

# Zkusim a uvidim

# Tady muzu a nemusim rozdelit na dva try-except bloky (v dalsim cviceni si budeme ukazovat lepsi pristup)
try:
    a = int(a_str)
    b = int(b_str)
except ValueError:
    print("Zadejte prosim cislo")
    exit()

try:
    print(a / b)
except ZeroDivisionError:
    print("Nulou nelze delit")


# 2 Čtení ze seznamu
# Uvažuj program, který čte knížku ze seznamu na základě indexu. Ošetři s použitím výjimky možnou chybu, že program skončí chybou.

knihy = ["Problém tří těles", "Temný les", "Vzpomínka na Zemi"]

# Osetrim a pak provedu

index = int(input("Zadej index knihy: "))

if index >= len(knihy):
    print("Zadany index neexistuje")
    exit()

# Zkusim a chytnu vyjimku

try:
    print(knihy[index])
except IndexError:
    print("Zadany index neexistuje")
    exit()


# [BONUS] 3 Datum
# Požádej uživatele o zadání data narození ve formátu RRRR-MM-DD.

# Nejprve ověř pomocí podmínek, že je zadáno správné datum - tj. v datu jsou dvě pomlčky
# a po rozdělení na jednotlivé části obsahuje každá z částí číslo.
# Stále je ale možné, že je zadáno nesmyslné datum. Například je možné zadat datum 31. dubna nebo 29. února pro nepřestupný rok.
# Proto přidej modul datetime a pomocí metody fromisoformat() vyzkoušej převod na typ datetime.
# Ošetři ValueError, která může být způsobena výše uvedenými případy.

# Zase vice zpusobu, ale treba takto:

from datetime import datetime

datum_narozeni = input("Zadej datum ve formátu RRRR-MM-DD: ")

# Osetrim a az pak provedu - tady uz je to trochu zbytecne moc prace (a to jsem asi ani nepokryla vsechny podminky ktere je vhodne osetrit)
for cast in datum_narozeni.split("-"):
    if not cast.isdigit():
        print("Datum musí obsahovat pouze číslice a pomlčky.")
        exit()

if datum_narozeni.count("-") != 2 :
    print("Datum musí být oddělené pomlčkami.")
    exit()

datum_narozeni = datetime.fromisoformat(datum_narozeni)

# Zkusim a uvidim
try:
    datum_narozeni = datetime.fromisoformat(datum_narozeni)
except ValueError:
    print("Zadané datum je ve spatnem formatu.", datum_narozeni)
    exit()
