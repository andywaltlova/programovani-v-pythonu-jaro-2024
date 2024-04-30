# 1 Výplata přesněji
# Zatím jsme výplatu počítali za předpokladu, že každý měsíc odpracujeme stejný počet hodin,
# což není příliš realistické. Stáhněte si textový soubor vykaz.txt, který obsahuje 12 řádků a na každém
# řádku počet odpracovaných hodin za každý měsíc za poslední rok.

# Otevřete tento soubor ve svém programu a načtěte hodnoty na řádcích do seznamu vykaz.
# Vytiskněte tento seznam do terminálu funkcí print() abyste si ověřili, že jste soubor načetli správně.
# Nechte uživatele zadat na příkazovém řádku hodinovou mzdu. Spočítejte a na výstup vytiskněte
# celkovou výplatu za celý rok a průměrnou výplatu na jeden měsíc.


# cesta = "/home/andy/Documents/programovani-v-pythonu-jaro-2024/08/data/vykaz.txt"
# vykaz = []
# with open(cesta, encoding='utf-8') as file:
#     for radek in file:
#         vykaz.append(int(radek.strip()))

# hodinova_mzda = int(input('Zadej hodinovou mzdu: '))

# soucet = 0
# for mesic in vykaz:
#     soucet += mesic * hodinova_mzda

# print(soucet)
# print(soucet / len(vykaz))


# 2 Počet slov
# Stáhněte si odevzdanou slohovou práci. Zadání bylo sepsat text o nejméně 150ti
# slovech pojednávající o našem hlavním městě. Napište program, který spočítá počet slov
# v tomto textu, abychom věděli, zda bylo zadání formálně splněno. Nechte se vést následujícím návodem.

# Nechte váš program otevřít soubor a načíst jednotlivé řádky do seznamu
# Každý řádek převeďte na seznam slov. Slovem se rozumí vše, co je odděleno mezerou nebo novým řádkem
# Vypište na výstup počty slov na každém řádku
# Vypište na výstup celkový počet všech slov v souboru

# radky = []
# cesta = "/home/andy/Documents/programovani-v-pythonu-jaro-2024/08/data/praha.txt"
# with open(cesta, encoding='utf-8') as file:
#     for line in file:
#         radky.append(line.strip())

# pocet_slov = 0
# for radek in radky:
#     slova_na_radku = radek.split()
#     print(len(slova_na_radku))
#     pocet_slov += len(slova_na_radku)

# print('Celkem slov: ', pocet_slov)

# [BONUS] 3.Půjčovna
# Půjčovna aut má v každém kraji ČR jedno auto s danou SPZ. Ke konci roku chce zjistit,
# kolik všechna auta najezdila dohromady kilometrů. V souboru auta.txt je pro každou SPZ
# zaznamenáno kolik dané auto ujelo kilometrů za daný rok. Hodnoty jsou v tisících kilometrů.
# Bohužel se v jednotlivých krajích blbě zkoordinovali a někdo používal desetinnou čárku, někdo zase tečku.

# Pozor! V souboru s daty je ještě jeden problém, který není na první pohled vidět!

# Napište program, který na výstup vypíše součet všech ujetých kilometrů.
# Jistě se vám bude hodit metoda řetězců jménem replace().

soucet_km = 0

cesta = '/home/andy/Documents/programovani-v-pythonu-jaro-2024/08/data/auta.txt'
with open(cesta, encoding='utf-8') as file:
    for line in file:
        hodnoty = line.split()  # rozdeleni podle mezery

        if len(hodnoty) > 1:  # protoze soubor ma jeden prazdny radek navic a jinak dostaneme IndexError
            km = hodnoty[1].replace(',', '.') # vymenim carku za tecku
            soucet_km += float(km)

print('Celkem ujeto: ', soucet_km * 1000, 'km')
# vynasobila jsem 1000 protoze v zadani psali ze to je v tisicich

