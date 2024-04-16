class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def __str__(self):
        return f"Adresa: {self.address} ({self.weight} Kg) - {self.state}"

    def delivery_price(self):
        if self.weight < 10:
            cena = 129
        elif self.weight < 20:
            cena = 159
        else:
            cena = 359
        return cena

    def deliver(self):
        if self.state == 'nedoruceno':
            self.state = 'doruceno'
            return 'Balik dorucen.'
        else:
            return f'Balik na adresu {self.address} jiz byl dorucen.'

class ValuablePackage(Package):
    def __init__(self, address, weight, state, value):
        super().__init__(address, weight, state)
        self.value = value

    def __str__(self):
        return super().__str__() + f" Cena = {self.value}"

#  1. Celková hodnota balíků
# Pokračuj ve své práci pro zásilkovou společnost. Společnost chce doplnit do aplikace funkci
# pro výpočet celkového hodnoty nákladu nějakého auta, aby pak (např. v případě nehody nebo krádeže)
# mohla snadno spočítat celkovou hodnotu cenných balíků v autě a předat informaci pojišťovně.
# Příklad je podobný bonusu na výpočet celkové hmotnosti z předchozí části, liší se ale v tom,
# že hodnotu mají pouze cenné balíky, zatímco hmotnost mají všechny balíky.

# Níže je příklad balíků, které můžeš použít pro tvorbu svého programu.

package_1 = ValuablePackage("Grimmauldovo náměstí 11", 1.9, "nedoručen", 5500)
package_2 = Package("Godrikův důl 47", 1.9, "nedoručen")
package_3 = ValuablePackage("Vydrník svatého Drába 13", 1.9, "nedoručen", 5500)
package_list = [package_1, package_2, package_3]

# Vytvoř si proměnnou total_value, do které si s využitím cyklu budeš ukládat celkovou hodnotu všech balíků. Na začátku bude mít hodnotu 0.
# Vytvoř cyklus, který projde seznam package_list.
# Vyber funkci, která je podle tebe nejvhodnější pro zajištění bezpečného čtení atributu value. Můžeš použít funkci isinstance(), hasattr() i getattr(). Přičti hodnotu balíku k proměnné total_value, aniž by program skončil chybou u objektu package_2.
# Na konci programu vypiš, jaká je celková hodnota balíků v autě.

# celková hodnota balíků v autě
total_value = 0

for one in package_list:
    if hasattr(one, 'value'):
        total_value += one.value

print(f'Celková hodnota balíků je {total_value},- Kč.')

# 2. Celková hodnota balíků podruhé
# Vedení společnosti si uvědomilo, že do hodnoty balíků v autě by se neměly započítávat balíky,
# které už byly doručeny, protože již byly předány příjemci a nebudou tedy ukradeny nebo zničeny.

# Uprav kód, který vytváří balíky, aby byl jeden balík vytvořený ve stavu doručen.
# Uprav cyklus, aby započítal hodnotu pouze těch balíků, které jsou ve stavu nedoručen.
# Je třeba pro čtení použít některou z funkcí isinstance(), hasattr() nebo getattr().

# je třeba jeden z balíků doručit
package_1.deliver()

# celková hodnota balíků v autě + rozšířit předchozí podmínku
total_value = 0

for one in package_list:
    if hasattr(one, 'value') and one.state == "nedoručen":
        total_value += one.value

print(f'Celková hodnota nedorucenych balíků je {total_value},- Kč.')


# 3. Vypravěči
# Nyní se vrátíme k práci pro nakladatelství, pro které jsme již připravili třídy Item, Book a AudioBook.
# V e-shopech se často objevuje možnost filtrování produktů. Uvažujme například, že někteří fanoušci a fanynky audioknih
# vybírají knihy podle herce a herečky, kteří je čtou. Preferované jméno bude uložené v proměnné favourite_narrator.
# Napiš kód, který projde všechny položky v seznamu all_items a vypíše názvy (atribut title) objektů,
# pro které se hodnota atributu narrator rovná hodnota v proměnné favourite_narrator.
# Pozor na to, že v seznamu all_items jsou i běžné knihy, které vypravěče nemají.
# Zajisti, aby program neskončil chybou, protože některý objekt nemá atribut narrator.

class Item:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def get_info(self):
        return f"{self.title} stojí {self.price} Kč."

    def get_time_to_read(self):
        pass

# Navic pages atribut
class Book(Item):
    def __init__(self, title, price, pages):
        super().__init__(title, price)
        self.pages = pages

    def get_info(self):
        return f"Kniha {self.title} má {self.pages} stran a stojí {self.price} Kč."

    def get_time_to_read(self, minutes=4):
        return self.pages * minutes / 60

# navic duration_in_hours a narrator
class AudioBook(Item):
    def __init__(self, title, price, duration_in_hours, narrator):
        super().__init__(title, price)
        self.duration_in_hours = duration_in_hours
        self.narrator = narrator

    def get_info(self):
        # Jen ukazka jak se treba popasovat s vypisem
        return super().get_info().replace('Kniha', 'Audiokniha')

    def get_time_to_read(self):
        return self.duration_in_hours

favourite_narrator = "Zbyšek Horák"
item_1 = AudioBook("Problém tří těles", 299, 14.4, "Zbyšek Horák")
item_2 = Book("Kadet Hornblower", 399, 242)
item_3 = AudioBook("Odysseus", 389, 13.7, "Lukáš Hlavica")

all_items = [item_1, item_2, item_3]


for one in all_items:
    if hasattr (one, 'narrator') and one.narrator == favourite_narrator:
        print(one.title)

###### PROVAZANI OBJEKTU ######

# 1. Auta a balíky
# U našich balíků budeme nově evidovat, který řidič(ka) balík doručuje.
# Díky tomu pak bude možné odeslat SMS zprávu s číslem řidiče (řidičky), aby mohli zákazníci v případě potřeby řidiče (řidičku) kontaktovat.

# Vytvoř třídu Driver, která bude mít atributy name a phone_number.
# Dále uprav třídu Package. Třída bude mít nově atribut driver, ve kterém bude uložen(a) řidič(ka) doručující balík.
# Uprav i třídu ValuablePackage, aby v metodě __init__() předala hodnotu parametru driver metodě __init__ rodičovské třídy.
# Přidej třídě Package metodu send_message(), která odešle zprávu s textem:
# "Dnes budeme doručovat váš balík. V případě potřeby kontaktujte řidiče na čísle: " Na konec zprávy doplň telefonní číslo.

from dataclasses import dataclass
@dataclass
class Driver:
    name: str
    phone_number: str

@dataclass
class Package:
    address: str
    weight: float
    state: str = 'nedoručen'
    driver: Driver = None

    def __str__(self):
        return f'Balík na adresu {self.address}, má hmotnost {self.weight} a je ve stavu {self.state}.'

    def delivery_price(self):
        if self.weight < 10:
            price = 129
        elif self.weight >= 10 and self.weight < 20:
            price = 159
        else:
            price = 359
        return price

    def deliver(self):
        if self.state == 'doručen':
            return f'Balík byl již doručen.'
        else:
            self.state = 'doručen'
            return f'Doručení uloženo.'

    def send_message(self):
        if self.driver is not None:
            message = f"Dnes budeme doručovat váš balík. V případě potřeby kontaktujte řidiče na čísle: {self.driver.phone_number}"
            print(f"Odesíláme SMS: {message}")

class ValuablePackage(Package):
    def __init__(self, address, weight, value, state='nedoručen', driver=None):
        super().__init__(address, weight, state, driver)
        self.value = value

    def __str__(self):
        return super().__str__() + f' Balík má hodnotu {self.value} Kč.'

# Příklad použití
driver_1 = Driver("Jana Nováková", "+420 123 456 789")


package_1 = ValuablePackage("Grimmauldovo náměstí 11", 1.9, 5000, "nedoručen", driver_1)
package_2 = Package("Godrikův důl 47", 1.9, "nedoručen")
package_3 = ValuablePackage("Vydrník svatého Drába 13", 1.9, 5500, "nedoručeno", driver_1)
package_list = [package_1, package_2, package_3]

package_1.send_message()

# Zbytek původního kódu pro výpočet celkové hodnoty balíků

total_value = 0

for one in package_list:
    if hasattr(one, 'value') and one.state == "nedoručen":
        total_value += one.value

print(f'Celková hodnota balíků je {total_value},- Kč.')
