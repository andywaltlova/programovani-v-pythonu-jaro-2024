# 1. Mějme seznam pohybů na nějakém bankovním účtu:

pohyby = [1200, -250, -800, 540, 721, -613, -222]

# Vypište v pořadí třetí pohyb z uvedeného seznamu.
print(pohyby[2])

# Vypište všechny pohyby kromě prvních dvou.
print(pohyby[2:])
# Vypište kolik je všech pohybů dohromady.
print(len(pohyby))

# Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb.
# min(), max()
print(f"Nejmensi hodnota: {min(pohyby)}")
print(max(pohyby))

# Spočítejte celkový přírůstek na účtu za dané období. Pozor, že přírůstek může vyjít i záporný.
print(sum(pohyby))


# 2. Mějme proměnnou s, ve které předpokládáme uložený nějaký seznam. Sestavte v výraz (vzoreček),
# který spočítá průměrnou hodnotu v takovém seznamu. Otestujte jej na seznamech různých délek.

znamky = [1,1,3,4,5]

prumer = sum(znamky) / len(znamky)
print(prumer)

# 3. Postupujte obdobně jako v úložce Průměr, ale tentokrát sestavte výraz pro výpočet rozpětí,
# tedy rozdílu mezi minimální a maximální hodnotou.
rozpeti = min(znamky) - max(znamky)
print(rozpeti)

# BONUSY
# 4. Sestavte výraz, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s.
# U seznamů liché délky je střed jasně definovaný, ovšem u seznamů sudé délky nám padne mezi dvě čísla.
# V takovém případě vyberte jako střed číslo blíže ke konci seznamu.
seznam_lichy = [1,2,3,4,5]
seznam_sudy = [1,2,3,4]
prostredek_lichy = len(seznam_lichy) // 2
prostredek_sudy = len(seznam_sudy) // 2

print(seznam_lichy[prostredek_lichy])
print(seznam_sudy[prostredek_sudy])


# 5. Sestavte vzoreček, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s.
# Tentokrát však u seznamů sudé délky vyberte jako střed číslo blíž k začátku seznamu.

# stejne jako predchozi, pripadne muzeme odecist -1 u sude delky

seznam_sudy = [1,2,3,4]

prostredek_vpravo = len(seznam_sudy) // 2
prostredek_vlevo = len(seznam_sudy) // 2 - 1