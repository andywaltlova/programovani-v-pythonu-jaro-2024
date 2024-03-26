# 1.Uvažujme vysvědčení, které máme zapsané jako slovník.

# Napiš program, který spočte průměrnou známku ze všech předmětů.
# Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.

school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

soucet_znamek = 0
for predmet in school_report.values():
    # vezmi znamku pricti ji do souctu
    # soucet = soucet + znamka
    soucet_znamek += predmet

# prumer = soucet znamek / pocet znamek
print(soucet_znamek / len(school_report))

# bez for cyklu s pomoci funkci
print(sum(school_report.values()) / len(school_report))


# Vypis predmetu se znamkou 1
for predmet, znamka in school_report.items():
    if znamka == 1:
        print(predmet)


# 2. Gustav je vášnivým čtenářem detektivek z našeho nakladatelství a navíc si zapisuje knihy, které přečetl.
# Níže ve slovníku vidíme, jaké informace si eviduje - název knihy, počet stran a hodnocení od 0 do 10.

# Napiš program, který spočte celkový počet stran, které Gustav přečetl.
# Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.
books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

soucet = 0
for kniha_slovnik in books:
    pocet_stran = kniha_slovnik['pages']
    soucet += pocet_stran

print(f'Soucet vsechn stran: {soucet}')

pocet_knih_hodnoceni_8 = 0
for kniha_slovnik in books:
    hodnoceni = kniha_slovnik['rating']
    if hodnoceni >= 8:
        pocet_knih_hodnoceni_8 += 1

print(f'Soucet knih s hodnocenim alespon 8: {pocet_knih_hodnoceni_8}')




## BONUSY
# 3. V následujícím slovníků je evidence automobilů.
# Klíčem jsou státní poznávací značky (SPZ) a hodnotou je jméno majitele vozu.
# Napiš program, který vypíše všechny majitele, jejichž vozidlo je registrováno v Plzeňském kraji,
# tj. na druhém místě (index 1!) řetězce v klíči je písmeno P.

plates = {
    "4A2 3000": "František Novák",
    "6P5 4747": "Jana Pilná",
    "3B7 3652": "Jaroslav Sečkár",
    "1P5 5269": "Marta Nováková",
    "37E 1252": "Martina Matušková",
    "2A5 2241": "Jan Král"
}

for spz, jmeno in plates.items():
    if 'P' == spz[1]:
        print(f'Je z Plzenskeho kraje: {jmeno}')

# 4. Recepty
# Pohlédněte na následující reprezentaci receptu:

recept = {
    'nazev': 'Batáty se šalvějí a pancettou',
    'narocnost': 'stredni',
    'doba': 30,
    'ingredience': [
        ['batát', '1', '15 kč'],
        ['olivový olej', '2 lžíce', '2 kč'],
        ['pancetta', '4-6 plátků', '21 kč'],
        ['přepuštěné máslo', '2 lžíce', '5 kč'],
        ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
        ['sůl', '1/2 lžičky', '0.1 kč'],
        ['muškátový oříšek', 'špetka', '1 kč'],
        ['česnek', '2 stroužky', '1 kč'],
        ['šalvějové lístky', '20-25', '12 kč']
    ]
}

# Uložte si tuto strukturu do proměnné recept na začátek nového programu.
# Vypište pomocí funkce print kolik bude celé jídlo stát korun zaokrouhlené na celé koruny nahoru.
import math

ingredience = recept['ingredience']
soucet = 0
for polozka in ingredience:
    cena_str = ingredience[-1]
    # Tady by teoreticky sla pouzit i split a vzit jen prvni prvek pred mezerou
    cena_cislo = int(cena_str.replace(' kč',''))
    soucet += cena_cislo

print(math.ceil(soucet))


