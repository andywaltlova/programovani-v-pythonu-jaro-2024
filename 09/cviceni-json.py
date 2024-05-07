import json
from pprint import pprint

# 1. Závod
# Pracuj dál se souborem zavod.json. Cílem cvičení je zjistit čas závodníka,
# který získal stříbrnou medaili - seznam závodníků je seřazený, tedy výherce je zapsán
# jako první v našem souboru. Budeš tedy muset projít data pomocí cyklu a vytvořit seznam
# všech závodníků, kteří závod dokončili, tj. jejich oficiální čas není 'DNF'.

# Můžeš postupovat následujícím způsobem:

# Vytvoř si prázdný seznam finishers, kam budeš vkládat jména závodníků, kteří závod doběhli.
# Pomocí cyklu projdi seznam závodníků.
# Do cyklu vlož podmínku, která ověří, zda oficiální čas závodníka je odlišná od řetězce DNF.
# Dovnitř podmínky vlož kód, který vloží jméno a oficiální čas závodníka do seznamu finishers.
# (obě hodnoty můžeš dát do nového seznamu, výsledný seznam finishers bude tedy obsahovat seznamy jako jeho položky).
# Pro přidání prvku do seznamu použij metodu append(), tedy finishers.append(seznam_s_jmenem_a_casem_zavodnika)
# Na konec programu (mimo cyklus) vlož příkaz na vypsání obsahu seznamu finishers.
# Zvol index výsledného seznamu finishers tak aby print vypisoval pouze stříbrného medailistu.
# U každého bodu si klidně ověř že tvůj aktuální kus kódu dělá to co má - například dočasným pomocným printem.


with open('data/zavod.json', mode='r', encoding='utf-8') as file:
    data = json.load(file)

finishers = []

for racer in data:
    casy = racer['casy']
    # oficialni_cas = casy['oficialni']
    oficialni_cas = casy.get('oficialni', None)
    if oficialni_cas != 'DNF':
        finishers.append([racer['jmeno'], oficialni_cas])

# pprint(finishers[1])


# 2 Transformace dat
# Stáhněte si soubor words.txt a zpracujte z něj výstupní soubor ve formátu JSON obsahující slovník.
# Klíče budou písmena a hodnoty seznamy slov, které začínají písmenem v klíči.
# Pokud na nějaké písmeno žádná slova nezačínají, tak ve výstupu toto písmeno nebude.
# Seřaďte tyto seznamy podle abecedy. Zajistěte, aby i klíče ve výstupním JSON souboru byly
# seřazeny a data byla odsazena čtyřmi mezerami pro lepší čitelnost člověkem.

# Priklad vystupniho formatu
# {
#     'a': ['apple', 'apricot', 'avocado'],
#     'b': ['banana', 'blueberry'],
# }

with open('data/words.txt', mode='r', encoding='utf-8') as file:
    lines = file.readlines()
    # for line in file:
    #     # ....

result = {}
for word in lines:
    word = word.strip()
    # slovnik[key] = value
    first_letter = word[0].lower()
    if first_letter in result:
        result[first_letter].append(word)
    else:
        result[first_letter] = [word]
    result[first_letter].sort()


with open('data/output.json', mode='w', encoding='utf-8') as file:
    json.dump(result, file, indent=4, sort_keys=True)


# BONUS
# 3 Narozeniny ve školce
# Toto pokročilé cvičení se úplně nedotýká formátu JSON, ale vyžaduje pokročilou
# práci se slovníky a hodně hledání na internetu.

# Paní ředitelka školky si exportovala z informačního systému seznam dětí,
# jejich zařazení do třídy a datum narození: kids.csv. Potřebuje vytvořit pro učitelky
# každé třídy výpis měsíců se seznamy dětí, které mají v tom měsíci narozeny.
# Výstupem budou textové soubory podle názvů tříd. Napište program univerzálně.
# Názvy tříd nejsou pevné, takže je získejte až ze samotných dat.


# POZOR TADY JE URCITE VIC RESENI, TOHLE BYLO PRVNI CO ME NAPADLO :)
import csv

with open ('kids.csv', mode='r', encoding='utf-8') as file:
    kids = csv.DictReader(file, delimiter=',', fieldnames=['name', 'class', 'bday'])
    kids_by_class = {}
    for kid in kids:
        trida = kid['class']
        if trida not in kids_by_class:
            # Pokud trida jeste neni ve vyslednem slovniku tak pridam prazdny slovnik
            kids_by_class[trida] = {}

        mesic = int(kid['bday'].split('.')[1])

        # Zadani nespecifikovalo tak jsem si rekla ze bude pekne ukladat jmeno i presny den
        narozeniny_jmeno_str = f'{kid["name"]} - {kid["bday"]}'

        if mesic not in kids_by_class[trida]:
            # Mesic jeste neni ve slovniku dane tridy
            kids_by_class[trida][mesic] = [narozeniny_jmeno_str]
        else:
            # Mesic uz ve slovniku dane tridy je, pridam jmeno do seznamu
            kids_by_class[trida][mesic].append(narozeniny_jmeno_str)

for trida, narozeniny in kids_by_class.items():
    with open(f'{trida}.json', mode='w', encoding='utf-8') as file:
        json.dump(narozeniny, file, indent=4, sort_keys=True, ensure_ascii=False)

