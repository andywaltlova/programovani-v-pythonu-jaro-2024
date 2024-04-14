# Úkol 1

Tvým úkolem bude vytvořit 4 třídy, které budou dohromady tvořit zoologickou zahradu. Doporučovala bych postupovat v pořadí ve kterém jsou třídy napsaný níže, bude to dávat největší smysl. Dodrzuj správnou strukturu souboru, tedy definice tříd děj nahoru pod sebe, samotné vytváření objektu a případné asserty na konec. Typování je dobrovolné.

## Třída `Zvire` 🦁 🐼 🐍

Tato třída bude obsahovat atributy `jmeno:str`, `druh:str` a `vaha:int`. Všechny parametry jsou povinné a budou se nastavovat v metodě `__init__()`

Dále přidej třídě `Zvire`:

* metodu `__str__()`, formát výpisu je na tobě
* metodu `export_to_dict()`, která vratí reprezentaci zvířete jako slovník, například takto:

```py
pavouk = Zvire('Adolf', 'Tarantule Velká', 0.1)
pavouk_export = pavouk.export_to_dict()
assert pavouk_export['jmeno'] == 'Adolf'
assert pavouk_export['druh'] == 'Tarantule Velká'
assert pavouk_export['vaha'] == 0.1
```

Vytvoř objekty typu `Zvire` z následujícího seznamu slovníků. Použij for cyklus, můžeš (ale nemusíš) to napsat jako funkci. Výsledkem bude list obsahující 4 objekty typu `Zvire`.

```py
zvirata_dict = [
    {'jmeno': 'Růženka', 'druh': 'Panda Velká', 'vaha': 150},
    {'jmeno': 'Vilda', 'druh': 'Vydra Mořská', 'vaha': 20},
    {'jmeno': 'Matýsek', 'druh': 'Tygr Sumaterský', 'vaha': 300},
    {'jmeno': 'Karlík', 'druh': 'Lední medvěd', 'vaha': 700},

]
```

## Třída `Zamestnanec` 🧑‍🤝‍🧑

Tato třída bude obsahovat atributy `cele_jmeno:str`, `rocni_plat:int` a `pozice:str`. Všechny parametry jsou povinné a budou se nastavovat v metodě `__init__()`

Zaměstnanci dále přidej:

* metodu `__str__()`, formát výpisu je na tobě
* metodu `ziskej_inicialy()`, která bude vracet výstup ve formátu `A.W.`, uvažuj pouze změstnance se dvěma jmény.

Vytvoř objekty typu `Zamestnanec` z následujícího seznamu slovníků. Použij for cyklus, můžeš (ale nemusíš) to napsat jako funkci. Výsledkem bude list obsahující 3 objekty typu `Zamestnanec`.

```py
zamestnanci_dict = [
    {'cele_jmeno': 'Tereza Vysoka', 'rocni_plat': 700_000, 'pozice': 'Cvičitelka tygrů'},
    {'cele_jmeno': 'Anet Krasna', 'rocni_plat': 600_000, 'pozice': 'Cvičitelka vyder'},
    {'cele_jmeno': 'Martin Veliky', 'rocni_plat': 650_000, 'pozice': 'Cvičitel ledních medvědů'},
]
```

## Třída `Reditel` 🧑‍💼

Tato třída bude dědit od třídy `Zamestnanec`, jediné co bude mít navíc je parametr `oblibene_zvire: Zvire`, parametr bude typu `Zvire` (třída kterou jsi už vytvořil/a). Parametr `pozice` rovnou nastav na `'Reditel'`.

```py
# Priklad vytvoreni objektu (klidne zkopiruj)
zvire = Zvire()
reditel = Reditel(jmeno='Karel', rocni_plat=800_000, oblibene_zvire=zvire)
assert reditel.pozice == 'Reditel'
assert isinstance(reditel.oblibene_zvire, Zvire)
```

## Třída `Zoo` 🏡

Třída `Zoo` bude mít 5 atributů:

* `jmeno:str`
* `adresa:str`
* `reditel: Reditel` - objekt typu `Reditel`
* `zamestnanci: List[Zamestnanec]` - list objektů typu `Zamestnanec` (naši vytvoření zaměstnanci)
* `zvirata: List[Zvire]` - list objektů typu `Zvire` (naše vytvořená zvířata)

a dvě metody:

*`vaha_vsech_zvirat_v_zoo()` - vrací číslo reprezentující součet váhy všech zvířat v zoologické zahradě
*`mesicni_naklady_na_zamestnance()` - vrací číslo reprezentující **měsíční** náklady na zaměstnance zoologické zahrady (Nezapomeň na ředitele!)

Příklad použití třídy:

```py
zoo = Zoo('ZOO Praha', 'U Trojského zámku 3/120', reditel, zamestnanci, zvirata)

print(zoo.reditel)
print('Celková váha zvířat v ZOO:', zoo.vaha_vsech_zvirat_v_zoo())
print('Měsíční náklady na zaměstnance:', zoo.mesicni_naklady_na_zamestnance())
```

## Asserty pro vlastní kontrolu ✔️

Následující asserty můžeš použít pro vlastní kontrolu, klidně si vytvoř i nějaké vlastní (nemusíš).

```py
# Zvire class
zvire = Zvire('Láďa', 'Koala', 15)
assert hasattr(zvire, 'jmeno')
assert hasattr(zvire, 'druh')
assert hasattr(zvire, 'vaha')
assert isinstance(zvire.jmeno, str)
assert isinstance(zvire.druh, str)
assert isinstance(zvire.vaha, int)
assert zvire.export_to_dict() == {'jmeno': 'Láďa', 'druh': 'Koala', 'vaha': 15}

# Zamestnanec class
zamestnanec = Zamestnanec('Petr Novak', 50000, 'Programator')
assert hasattr(zamestnanec, 'cele_jmeno')
assert hasattr(zamestnanec, 'rocni_plat')
assert hasattr(zamestnanec, 'pozice')
assert isinstance(zamestnanec.cele_jmeno, str)
assert isinstance(zamestnanec.rocni_plat, int)
assert isinstance(zamestnanec.pozice, str)
assert zamestnanec.ziskej_inicialy() == 'P.N.'

# Reditel class
zvire = Zvire('Lev', 'Lvice', 150)
reditel = Reditel('Jan Novotny', 80000, zvire)
assert isinstance(reditel.oblibene_zvire, Zvire)

# Zoo class
zoo = Zoo('Zoo Praha', 'Praha', reditel, [zamestnanec], [zvire])
assert hasattr(zoo, 'nazev')
assert hasattr(zoo, 'adresa')
assert hasattr(zoo, 'reditel')
assert hasattr(zoo, 'zamestnanci')
assert hasattr(zoo, 'zvirata')
assert isinstance(zoo.nazev, str)
assert isinstance(zoo.adresa, str)
assert isinstance(zoo.reditel, Reditel)
assert isinstance(zoo.zamestnanci, list)
assert isinstance(zoo.zvirata, list)
assert zoo.vaha_vsech_zvirat_v_zoo() == 150
assert zoo.mesicni_naklady_na_zamestnance() == (zamestnanec.rocni_plat + reditel.rocni_plat) / 12
```
