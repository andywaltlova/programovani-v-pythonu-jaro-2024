# https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/vyjimky/pokrocila-prace

import sys

# 1 Banka
# Nasimulujme si fungování bankovní aplikace, konkrétně žádost o převod peněz z účtu.

# Na začátku si vytvoř program balance.txt a do něj vlož nějaké číslo.
# Toto číslo reprezentuje aktuální zůstatek na účtu.

# Přečti hodnotu v souboru, převeď ji na číslo a ulož ji do proměnné account_balance.
# Čtení souboru i převod na číslo ošetři pomocí výjimek.

try:
    with open("data/balance.txt", "r") as file:
        account_balance = file.read()
        account_balance = float(account_balance)
except FileNotFoundError:
    print("Soubor neexistuje.")
    sys.exit()
except ValueError:
    print("Soubor neobsahuje číslo.")
    sys.exit()

# Následně se zeptej uživatele (uživatelky), kolik peněz chce převést na jiný účet.
# Ošetři pomocí výjimky, že uživatel (uživatelka) zadal(a) číslo.

try:
    castka = int(input("Kolik peněz chcete převést na jiný účet?: "))
except ValueError:
    print("Castka musi byt cislo")
    sys.exit()

# Dále vyvolej ValueError v případě, že zadaná částka je záporná nebo vyšší než zústatek na účtu.
# Pokud je vše v pořádku, spočítej nový zůstatek a zapiš ho do souboru balance.txt.

if castka < 0:
    raise ValueError("Zápornou částku nelze převést.")
if castka > account_balance:
    raise ValueError("Nemáte dostatek peněz na účtu.")

# Probehne to odecteni penez
account_balance -= castka
with open("data/balance.txt", "w") as file:
    file.write(str(account_balance))



# [BONUS] 2 Úkoly
# Implementujme systém pro správu seznamu úkolů (todo list). Stáhni si soubor tasks.txt.
# Každý řádek obsahuje název úkolu a jeho prioritu (1=vysoká, 2=střední, 3=nízká), hodnoty jsou oddělené čárkou.

# Tvůj program by měl nejprve načíst existující úkoly ze souboru `tasks.txt`` a uložit je do seznamu.
# Pokud soubor neexistuje, program jen vypíše informaci o tom, že seoubor neexistuje a že ho založí.
# Samotné založení souboru v této části řešit nemusíš, o to se postaráme v další části.

# Poté program umožní uživateli přidat nový úkol a jeho prioritu. Pokud jako prioritu nezadá číslo nebo zadá jiné číslo než 1 až 3,
# vyvolej ValueError. Pokud je vstup v pořádku, ulož seznam s přidaným úkolem do souboru tasks.txt.
# Pokud soubor neexistuje, stačí ho pomocí funkce open s módem w otevřít.

try:
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
except FileNotFoundError:
    print("Soubor neexistuje.")
    tasks = []

task = input("Zadej název úkolu: ")

priority = int(input("Zadej prioritu úkolu (1-3): "))
if priority not in [1, 2, 3]:
    raise ValueError("Priorita musí být 1, 2 nebo 3.")

tasks.append(f"{task},{priority}\n")

with open("tasks.txt", "w") as file:
    file.writelines(tasks)
