# 1 Dny v měsíci
# Napište program, který bude mít přímo v kódu zapsaný počet dní v jednotlivých měsících takto:

pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Nechte váš program vypsat tento seznam do souboru s názvem kalendar.txt, každé číslo na jeden řádek.


with open('data/kalendar.txt', mode='w') as file:
    for den in pocty_dni:
        print(den, file=file)

        # Alternativne metoda write
        file.write(f"{den}\n")


# 2 Vytvoření souboru
# Napište program, který se po spuštění zeptá na název souboru, který má vytvořit
# (nebo přepsat, pokud už ten soubor existuje), a pak se zeptá na řádek textu, který má do souboru zapsat.


soubor = input('Zadej nazev souboru: ')
text = input(f'Zadej text pro zapis do {soubor}.txt: ' )


with open(f"data/{soubor}.txt", mode='w') as file:
    print(text, file=file)



# 3 Rozepsaná výplata
# Modifikujte program pro počítání výplaty z předchozí sekce tak, aby nevypisoval průměrnou
# výplatu za rok, nýbrž aby vypsal konkrétní vyplacenou částku pro každý měsíc zvlášť.

# Nejprve tyto informace vypište na terminál
# Poté program upravte tak, aby vypsal tyto výsledky do souboru


cesta = "/home/andy/Documents/programovani-v-pythonu-jaro-2024/08/data/vykaz.txt"
vykaz = []
with open(cesta, encoding='utf-8') as file:
    for radek in file:
        vykaz.append(int(radek.strip()))

hodinova_mzda = int(input('Zadej hodinovou mzdu: '))


with open('data/vyplaty.txt', mode='w') as file:
    for mesic in vykaz:
        print(mesic * hodinova_mzda, file=file)


