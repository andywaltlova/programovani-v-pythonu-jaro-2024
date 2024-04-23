# https://kodim.cz/czechitas/python-data-1/bonusy/datum/datum

from datetime import datetime, timedelta


apollo_start = datetime(1969, 7, 16, 14, 32)

# 1. Prevod casu
# V proměnné apolloStart máme uložený datum a čas startu Apolla 11.
# Vypiš datum na obrazovku ve formátu, na který jsou zvyklí Američané,
# tj. na první místo napiš měsíc, dále den a nakonec rok, jako oddělovače použij lomítka.
# Čas vypisovat nemusíš.
# Očekávaný výstup: 7/16/1969

print(apollo_start.strftime("%m/%d/%Y"))


# 2. Čas od startu
# Satelit Solar Orbiter, který má za cíl pozorování Slunce, odstartoval 10. února 2020 v 5:03.
# Ulož si hodnotu startu do proměnné.

# Který den v týdnu Solar Orbiter odstartoval?
start_solar_orbiter = datetime(year=2020, month=2, day=10, hour=5, minute=3)
den_v_tydnu: str = start_solar_orbiter.strftime("%A")
den_v_tydnu_cislovka: int = start_solar_orbiter.weekday()
print(den_v_tydnu, den_v_tydnu_cislovka)

# Spočítej, kolik času od jeho startu uplynulo.
dnes = datetime.now()
uplynulo = dnes - start_solar_orbiter
print(uplynulo)

# 3 Doprava večeře
# Zákazník si objednal večeři na webu dovážkové služby 13. listopadu 2020 v 19:47.
# Víme, že převzetí objednávky restaurací v průměru trvá 8 minut a 35 sekund, příprava jídla trvá 30 minut
# a doprava jídla k zákazníkovi 25 minut a 30 sekund. Kdy očekáváme, že jídlo dorazí zákazníkovi?

cas_objednani = datetime(2020, 11, 13, 19, 47)

prevzeti_objednavky = timedelta(minutes=8, seconds=35)
priprava_jidla = timedelta(minutes=30)
doprava = timedelta(minutes=25, seconds=30)

ocekavany_cas = cas_objednani + prevzeti_objednavky + priprava_jidla + doprava
print(ocekavany_cas)

