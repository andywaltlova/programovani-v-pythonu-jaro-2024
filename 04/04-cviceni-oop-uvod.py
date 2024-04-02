# Lekce
class Employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement

    def get_info(self):
        return f'Zaměstnanec {self.name} pracuje jako {self.position}.'


jirka = Employee('Jiří', 'konstruktér', 25)
jakub = Employee('Jakub', 'konstruktér', 25)
zamestnanci = [jakub, jirka]

################################################################################


# 1. Balik - https://kodim.cz/czechitas/python-oop/lekce/tridy/tridy/balik
# Uvažuj, že navrhuješ software pro zásilkovou společnost.

# Vytvoř třídu Package, která bude mít tři atributy - address, weight a state.
# Vytvoř metodu __init__, která uloží hodnoty parametrů metody do atributů.

# Přidej metodu get_info(), která vrátí informace o balíku jako řetězec.
# Uvažuj například větu "Balík na adresu Václavské Náměstí 12, Praha má hmotnost 0.25 kg je ve stavu nedoručen".

# Zkus si vytvořit alespoň dva objekty ze třídy Balik.
# U address uvažujeme typ řetězec (str), u weight desetinné číslo.
# U atributu state zadávej pro zjednodušení pouze dva stavy: doručen a nedoručen.

# Vypiš informace, které generuje metoda get_info(), na obrazovku, a ověř, že je vše v pořádku.

# Vytvoř metodu delivery_price(), která vypočítá cenu přepravy balíku.
# Cena přepravy je daná hmotností balíku.
# Cena přepravy balíku do 10 kg je 129 Kč, cena přepravy balíku od 10 kg do 20 kg je 159 Kč
# a cena přepravy balíků těžších než 20 kg je 359 Kč. Metoda spočítá cenu a vrátí ji jako číslo.


class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def get_info(self):
        return f"Adresa: {self.address} ({self.weight} Kg) - {self.state}"

    def delivery_price(self):
        if self.weight < 10:
            cena = 129
        elif self.weight < 20:
            cena = 159
        else:
            cena = 359
        return cena



balik_1 = Package('Praha', 15, True)
balik_2 = Package('Brno', 25, False)
balik_3 = Package('Ostrava', 5, False)

print(balik_1.delivery_price())
print(balik_2.delivery_price())
print(balik_3.delivery_price())



# 2 Kniha
# Zkus pro nakladatelství vytvořit software s využitím tříd a objektů.
# Vytvoř tedy třídu Book, která reprezentuje knihu. Každá kniha bude mít atributy title, pages a price.
# Hodnoty nastav ve funkci __init__.

# Přidej knize funkci get_info(), která vypíše informace o knize v nějakém pěkném formátu.
# Přidej metodu get_time_to_read(). Metoda vrátí čas potřebný na přečtení knihy v hodinách.
# S využitím atributu pages vypočítej čas na přečtení knihy.
# Metoda bude mít nepovinný parametr, který udává počet minut potřebných pro přečtení jedné stránky knihy.
# Dobu potřebnou na přečtení knihy získáš jako násobek doby potřebné na přečtení jedné stránky knihy
# a počet stránek knihy. Výchozí hodnota nepovinného parametru je 4.

class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price

    def get_info(self):
        return f"Kniha {self.title} má {self.pages} stran a stojí {self.price} Kč."

    def get_time_to_read(self, minutes=4):
        return self.pages * minutes / 60

kniha = Book('Vražda s příliš mnoha notami', 450, 300)
print(kniha.get_info())