# https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/vlastni-funkce/excs

# 1. Násobení
# Napiš funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek.

def mult (a,b):
    return a*b

mult(15,9)

# 2. Funkce pro převody jednotek
# https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/vlastni-funkce/excs/prevody-jednotek

# Staci treba dve, vsechny jsou na stejny princip :)

def kilometry_na_mile(kilometry):
    return kilometry * 0.621371192

def mily_na_kilometry(mile):
    return mile * 1.609344


# [BONUS] 3. Rámeček
# Napiš funkci, která jako parametr převezme řetězec a vytiskne jej obalen hvězdičkami.

# Zadej slovo: ahoj
# ********
# * ahoj *
# ********
# Nápověda: 8 * '*' == '********'

# Bonus: Znak, kterým se má text obalit, bude zadán také jako parametr.

def ramecek (slovo):
    ohraniceni = '*' * ((len(slovo))+5)
    print(ohraniceni)
    print('* ' + slovo + ' *')
    print(ohraniceni)

slovo = input('Zadejte slovo, které chcete umístit do rámečku:\n')

ramecek(slovo)

# úsporná varianta

def ramecek (slovo):
    ohraniceni = '*' * ((len(slovo))+5)
    print(ohraniceni + '\n' + '* ' + slovo + ' *' + '\n' + ohraniceni)

slovo = input('Zadejte slovo, které chcete umístit do rámečku:\n')

ramecek(slovo)

# bonus
def ramecek (slovo, znak):
    ohraniceni = znak * ((len(slovo))+5)
    print(ohraniceni)
    print('* ' + slovo + ' *')
    print(ohraniceni)

slovo = input('Zadejte slovo, které chcete umístit do rámečku:\n')

znak = input('Zadejte znak, kterým chcete mít orámované slovo:\n')

ramecek(slovo, znak)

# [BONUS] 4. Měsíc narození
# Napiš funkci month_of_birth, která bude mít jeden parametr - rodné číslo.
# Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup.
# Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.

# Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5.

def month_of_birth(rodne_cislo):
    mesic = int(rodne_cislo[2:4])
    if mesic > 12:
        mesic -= 50
        print(mesic)
    else:
        print(mesic)
month_of_birth('9207054439')
month_of_birth('9555125899')

