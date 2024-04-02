# 1. Balik podruhe
# Vrať se k návrhu software pro zásilkovou společnost.

# U třídy Package přejmenuj metodu get_info() na __str__() a vyzkoušej,
# jestli nyní stačí k získání informací o balíku funkce print().

# Přidej metodu deliver(). Půjde o obdobu tlačítka, které řidič nebo řidička zmáčkne
# při doručení balíku a zaznamená tak jeho doručení. Metoda nejprve zkontroluje,
# zda balík náhodou již není ve stavu doručen. Pokud ano, metoda vrátí zprávu "Balík již byl doručen".
# Tím bude řidič (řidička) informován(a) o tom, že se pravděpodobně spletl(a) a snaží se zaznamenat
# doručení u špatného balíku. Pokud balík není ve stavu doručen, změň jeho stav právě na doručen a vrať zprávu
# "Doručení uloženo".

# Vyzkoušej metodu deliver(). Co se stane, pokud ji u jednoho balíku zavoláš dvakrát?


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

balik_A = Package('A', 10, 'doruceno')
balik_B = Package('B', 10, 'nedoruceno')

print(balik_A)
print(balik_B)
print(balik_A.deliver())
print(balik_B.deliver())

# 2. Kniha podruhe
# Vrať se k práci se třídou Book. Pokud jsi ji nestihl(a) v minulé části vytvořit,
# vrať se nejprve k zadání příkladu na předchozí stránce a třídu si vytvoř.

# U knihy budeme chtít evidovat, kolik kusů bylo prodáno. Přidej atribut sold, jehož hodnotu bude možné nastavit v metodě __init__().
# Dále přidej atribut costs, které představují náklady na jednu knihu (např. tisk, doprava do knihkupectví, podíl autora (autorky) atd.).

# Přidej metodu profit(), která vrátí celkový zisk z knihy. Zisk vypočti na základě vzorce: prodané kusy * (cena - náklady).

# Přidej metodu rating(), která vrátí hodnocení knihy na základě jejího zisku. Pokud bude zisk méně než 50 tisíc, vrať hodnotu "propadák".
# Pokud bude zisk mezi 50 tisíc a 500 tisíc, vrať hodnotu "průměr". Pokud bude vyšší než 500 tisíc, vrať hodnotu "bestseller".

class Book:
    def __init__(self, title, pages, price, sold, costs):
        self.title = title
        self.pages = pages
        self.price = price
        self.sold = sold
        self.costs = costs

    def profit(self):
        return self.sold * (self.price - self.costs)

    def rating(self):
        if self.profit() < 50000:
            return 'propadak'
        elif self.profit() < 500000:
            return 'prumer'
        else:
            return 'bestseller'

    def get_info(self):
        return f"Kniha {self.title} má {self.pages} stran a stojí {self.price} Kč."

    def get_time_to_read(self, minutes=4):
        return self.pages * minutes / 60

kniha = Book('Vražda s příliš mnoha notami', pages=450, price=359, sold=1000, costs=100)
print(kniha.get_info())
print(kniha.rating())

# 3. Zkušební doba
# U zaměstnanců budeme nově evidovat, jestli jsou ve zkušební době.

# Rozšiř metodu __init__ třídy Employee o parametr probation_period. Tuto hodnotu ulož jako atribut třídy Employee.
# Uprav metodu __str__. Pokud je zaměstnanec ve zkušební době, přidej k jeho/jejímu výpisu text Je ve zkušební době.


class Employee:
    def __init__(self, name, position, holiday_entitlement, probation_period):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
        self.probation_period = probation_period

    def __str__(self):
        zakladni_vypis = f"{self.name}({self.position}) - {self.holiday_entitlement} dni dovolene."
        if self.probation_period:
            return zakladni_vypis + ' Je ve zkusebni dobe.'
        else:
            return zakladni_vypis

    def get_info(self):
        return f'Zaměstnanec {self.name} pracuje jako {self.position}.'


# 4 Seznam balíků
# Přepravní společnost musí rozdělovat balíky do jednotlivých aut. Při plánování dopravy je potřeba hlídat,
# zda pro jeden automobil není naplánována přeprava příliš velkého množství balíků.
# Vytvoř tedy tři objekty třídy Package. Dále vytvoř seznam package_list, do kterého vlož vytvořené objekty. Příklad objektů a seznamu je níže.

package_1 = Package("Grimmauldovo náměstí 11", 15, "nedoručen")
package_2 = Package("Godrikův důl 47", 3, "nedoručen")
package_3 = Package("Vydrník svatého Drába 13", 0.5, "nedoručen")
package_list = [package_1, package_2, package_3]

# Vytvoř si proměnnou total_weight, do které si s využitím cyklu budeš ukládat celkovou hmotnost všech balíků. Na začátku bude mít hodnotu 0.
# Vytvoř cyklus, který projde seznam package_list.
# Pro každý balík přičti jeho hmotnost k proměnné total_weight.
# Na konci programu vypiš, jaká je celková hmotnost všech balíků.

total_weight = 0
for package in package_list:
    total_weight += package.weight

print(f"Celkova hmotnost vsech baliku je {total_weight} Kg.")

# Zatím jsme uvažovali, že třídu Package využívá ve svém programu přepravní společnost.
# Stejnou třídu by ale mohl používat e-shop, který takto eviduje zboží odeslané zákazníkům.
# Provozovatele e-shopu bude určitě zajímat, kolik celkem zaplatí přepravní společnosti za přepravu balíku.
# Využij tedy balíky v seznamu package_list a spočítej celkové náklady na jejich přepravu.
# Náklady na přepravu jednoho balíku zjistíš voláním metody delivery_price().

total_price = 0
for package in package_list:
    total_price += package.delivery_price()

print(f"Celkove naklady na prepravu baliku jsou {total_price} Kc.")