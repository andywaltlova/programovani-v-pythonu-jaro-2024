# pip3 install requests

import requests
from pprint import pprint

# 1. Seznam lidí
# Jak už jsme si ověřili v lekci, datové API na adrese
# https://api.kodim.cz/python-data/people obsahuje seznam lidí.
# Napište program, který tento seznam z API stáhne a převede z formátu JSON na Python slovníky.

response = requests.get('https://api.kodim.cz/python-data/people')
data = response.json()
# print(data)
# pprint(data)

# Proveďte následující úkoly.
# Zjistěte kolik lidí celkem seznam obsahuje.
print(len(data))
# Zjistěte jaké všechny informace máme o jednotlivých osobách.
print(data[0].keys())
# Zjistěte, kolik je v souboru mužů a žen.
muzi = 0
for person in data:
    if person['gender'] == 'Male':
        muzi += 1

# Teoreticky by se dalo dopocitat z celkoveho poctu pokud mame v datech jen dve pohlavi
# zeny = len(data) - muzi

zeny = 0
for person in data:
    if person['gender'] == 'Female':
        zeny += 1

print(f'Muzi: {muzi}, Zeny: {zeny}')


# 2 Svátky
# Na adrese https://svatky.adresa.info/json najdete API, které vám odpoví, kdo má dneska svátek.

# Využijte toto API k tomu, abyste napsali program, který po spuštění vypíše na obrazovku kdo má dneska svátek.
# Pokud použijete adresu https://svatky.adresa.info/json?date=DDMM, kde místo DDMM doplníte datum, dostanete jméno,
# které má svátek v zadaný den. Formát DDMM znamená že 6. ledna bude zapsáno jako 0601, 12. září jako 1209 apod.
# Napište program, který dostane na příkazové řádce číslo dne a číslo měsíce a vypíše na výstup kdo má v daný den svátek.
# Použijte váš program abyste zjistili, kdo má svátek 29. února.
# Bonus: předchozí bod uprav tak, že nebudeš dávat funkci requests.get() adresu včetně parametru date=1209,
# ale pouze základní "endpoint" https://svatky.adresa.info/json a parametry (vše za ?) dodáš volitelným parametrem.
# Budeš potřebovat pracovat s dokumentací k requests.

response = requests.get('https://svatky.adresa.info/json')
data = response.json()
print(data)
print(data[0]['name'])


# Se zadanim data

# date = input('Zadej datum ve formatu DDMM: ')
# DDMM
date = '2412'
response = requests.get(f'https://svatky.adresa.info/json?date={date}')
# response = requests.get('https://svatky.adresa.info/json?date=' + date)

print(response.json())
for jmeno in response.json():
    print(jmeno['name'])

