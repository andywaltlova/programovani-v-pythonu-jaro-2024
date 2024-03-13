# 1. Uložte si do proměnné jmeno svoje jméno.
# Pomocí volání vhodných metod jej převeďte nejdříve na malá písmena a poté na velká písmena.

jmeno = "Andrea"

print(jmeno.lower())
print(jmeno.upper())

# 2. Mějme seznam celých čísel zadaných jako text

hodnoty = ['12', '1', '7', '-11']

print(hodnoty)
cislo = hodnoty[2]
cislo = int(cislo)
cislo += 4
cislo = str(cislo)

hodnoty[2] = cislo

print(hodnoty)

# Potřebujeme k třetímu číslu v seznamu přičíst 4, aby výsledek vypadal takto:
# hodnoty = ['12', '1', '11', '-11']


# 3. Máme obdobné zadání jako v předchozím cvičení, avšak tentokrát máme čísla zadána nikoliv v seznamu,
# ale v řetězci oddělená mezerou:

hodnoty = '12.1 1.68 7.45 -11.51'

# K poslednímu číslu v seznamu chceme přičíst 0.25 tak, aby výsledek vypadal takto
# hodnoty = '12.1 1.68 7.45 -11.26'
# Určitě se vám budou hodit metody split a join.

rozdelena_cisla = hodnoty.split(' ')
nove_cislo = float(rozdelena_cisla[-1]) + 0.25
rozdelena_cisla[-1] = str(nove_cislo)

print(" ".join(rozdelena_cisla))


# BONUS
# Zkuste vymyslet, jak udělat zápis příkazů ze cvičení Čísla jako text (2.) co nejúspornější.
# Dá se dojít až k tomu, že celé řešení bude na jeden řádek.

hodnoty = ['12', '1', '7', '-11']
hodnoty[2] = str(int(hodnoty[2]) + 4)
print(hodnoty)
