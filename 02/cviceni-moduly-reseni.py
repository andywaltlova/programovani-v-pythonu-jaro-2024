# https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/slicing-metody-moduly/moduly

# 1 Zaokrouhlování
# Napište program, který dostane na vstupu desetinné číslo a na výstup napíše
# toto číslo zaokrouhlené nejdříve nahoru, potom dolů a potom běžným Pythonovským zaokrouhlováním.

# TODO

# [BONUS] 2.Přijímačky a moduly
# Uvažujme vysvědčení studenta, které máme uložené jako seznam.

school_report = [
    ["Český jazyk", 1],
    ["Anglický jazyk", 1],
    ["Matematika", 1],
    ["Přírodopis", 2],
    ["Dějepis", 1],
    ["Fyzika", 2],
    ["Hudební výchova", 4],
    ["Výtvarná výchova", 2],
    ["Tělesná výchova", 3],
    ["Chemie", 4],
]
# Uvažuj, že student se hlásí na školu, která vybírá studenty podle průměru.
# Pro školu jsou ale důležité pouze předměty český jazyk, anglický jazyk, matematika a fyzika.
# Vypočítej průměr studenta z daných předmětů s využitím modulu statistics.
# Na začátku vytvoř prázdný seznam a následně pomocí cyklu vlož do nového seznamu
# známky ze čtyř vyjmenovaných předmětů. Nakonec použij metodu statistics.mean() k výpočtu průměru.
# Dále zkus využít funkce, které jsou zmíněné v textu, k výpočtu nejlepší a nejhorší známky z daných předmětů.

# TODO

# [BONUS] 3. Vánoční party
# Ve statistice existuje ukazatel zvaný modus, který vrátí nejčastější hodnotu v datech.
# V modulu statistics existuje funkce mode(), která umí modus spočítat.
# Funkce mode() má navíc vychytávku, umí pracovat i s řetězci.

# Uvažuj data v seznamu votes, což je hlasování zaměstnanců malé firmy o tom, jakou akci podniknou
# během jejich vánočního večírku. Použij funkce mode() ke zjištění, pro jakou aktivitu hlasovalo
# nejvíce zaměstnanců. Funkce má jeden parametr - seznam, ze kterého má určit nejčastější prvek.

votes = [
    "curling",
    "vánoční svařák na trzích",
    "vánoční svařák na trzích",
    "curling",
    "zážitková první pomoc",
    "curling",
    "zážitková první pomoc",
    "curling",
    "zážitková první pomoc",
]

# Můžeš se podívat i na popis funkce v dokumentaci (https://docs.python.org/3/library/statistics.html#statistics.mode),
# která obsahuje i příklad s použitím řetězců.

# TODO
