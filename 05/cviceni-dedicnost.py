# https://kodim.cz/czechitas/python-oop/lekce/dedicnost/dedicnost

# 1. Pokračuj ve své práci pro zásilkovou společnost.
# Společnost nově doručuje i cenné balíky, které mají zadanou určitou hodnotu.

# Vytvoř třídu ValuablePackage, která dědí od třídy Package.
# ValuablePackage má navíc atribut value, ostatní atributy dědí od třídy Package.
# Atribut value nastav pomocí funkce __init__. Ostatní parametry předej
# funkci __init__ třídy Package.
# Přidej do výpisu informací o cenném balíku (metoda __str__) informaci o ceně balíku.
# Vytvoř si alespoň jeden objekt a zkus volání jeho funkcí.
# Současně si vytvoř "obyčejný" balík o zkontroluj, že u něj se nic nezměnilo.

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

# 2 Cena přepravy
# Pokračuj ve své práci pro zásilkovou společnost. Společnost nově požaduje,
# aby náš software uměl dopočítat cenu přepravy balíku.

# U cenných balíků bude k ceně připočteno pojištění. Přidej ke třídě
# ValuablePackage metodu delivery_price().
# Ta spočítá cenu přepravy s využitím metody mateřské třídy Package,
# kterou jsme vytvořili v předchozí lekci.
# K tomu připočte pojistné ve výši 5 % ceny balíku.

class ValuablePackage(Package):
    def __init__(self, address, weight, state, price):
        super().__init__(address, weight, state)
        self.price = price

    def __str__(self):
        return super().__str__() + f" Cena = {self.value}"

    # navic vlastni upravena metoda delivery_price()
    def delivery_price(self):
        cena_ze_tridy_package = super().delivery_price()
        pet_procent = self.price * 0.05

        return cena_ze_tridy_package + pet_procent


balik1 = ValuablePackage ("Vinohradská 15", 100, "nedoručen", 300)
print(balik1.delivery_price())


obyc_balik = Package('Usti nad Labem', 23, 'dorucen')
# print(obyc_balik.delivery_price())
cennej_balik = ValuablePackage('Usti nad Labem', 23, 'dorucen', 3500)
# print(cennej_balik.delivery_price())

## BONUSY

# 3 Jízdenky a letenky
# Nyní je naším cílem práce pro společnost, která se zabývá prodejem jízdenek a letenek.

# Vytvoř třídu Ticket, která bude mít atributy basic_price (základní cena) a seat_number (číslo sedadla).
# Tato třída bude sloužit například pro cesty autobusem. Při cestování vlakem musíme řešit, jestli cestující využívá 1. nebo 2. třídu.
# Vytvoř třídu TrainTicket,
# která bude mít navíc atribut fare_class (uvažujeme možnosti economy a business). Dále naprogramuj metodu get_price(),
# která bude vracet hodnotu stejnou jako basic_price, pokud atribut fare_class je economy, a cenu o 30 % vyšší oproti basic_price,
# pokud fare_class je business.

# U letenek řešíme třídu, kterou cestující letí, navíc ale musíme řešit i počet odbavených zavazadel. Vytvoř třídu PlaneTicket,
# která bude dědit od třídy TrainTicket a bude mít navíc atribut checkout_luggages, který udává počet odbavených zavazadel.
# Naprogramuj metodu get_price(),
# která bude vracet hodnotu stejnou jako basic_price, pokud atribut fare_class je economy,
# a cenu o 50 % vyšší oproti basic_price, pokud fare_class je business.
# Dále připočti 2000 za každé odbavené zavazadlo (bez ohledu na třídu).

# Vytvoř jízdenku na vlak se základní cenou 150 do tříd economy i business. Zkontroluj, jakou hodnotu vrací metoda get_price().
# Vytvoř letenku se základní cenou 6000 do tříd economy i business s jedním odbaveným zavazadlem. Zkontroluj, jakou hodnotu vrací metoda get_price().
# Vyzkoušej vypočítat celkovou cenu dvou jízdenek různého typu, tj. jedné letenky a jedné jízdenky na vlak. Celkovou cenu ulož do proměnné
# total_price a k výpočtu použij metodu get_price().

class Ticket:
    def __init__(self, basic_price, seat_number):
        self.basic_price = basic_price
        self.seat_number = seat_number

    def get_price(self):
        return self.basic_price


class TrainTicket(Ticket):
    def __init__(self, basic_price, seat_number, fare_class):
        super().__init__(basic_price, seat_number)
        self.fare_class = fare_class

    def get_price(self):
        # if self.fare_class == 'economy':
        #     return self.basic_price
        if self.fare_class == 'business':
            return self.basic_price + (self.basic_price * 0.3)
        return self.basic_price

class PlaneTicket(TrainTicket):
    def __init__(self, basic_price, seat_number, fare_class, checkout_luggages):
        super().__init__(basic_price, seat_number, fare_class)
        self.checkout_luggages = checkout_luggages

    def get_price(self):
        cena = self.checkout_luggages * 2000
        if self.fare_class == 'economy':
            cena += self.basic_price
        if self.fare_class == 'business':
            cena += self.basic_price + (self.basic_price * 0.5)
        return cena


# listek_na_autobuse = Ticket(20, 54)
# listek_na_vlak_e = TrainTicket(150, 15, 'economy')
# listek_na_vlak_b = TrainTicket(150, 15, 'business')
# letenka_e = PlaneTicket(300, 15, 'economy', 1)
# letenka_b = PlaneTicket(300, 15, 'business', 1)


# 4 Audioknihy
# V některých případech je nutné sáhnout k úpravám již napsané třídy. Uvažujme nakladatelství, pro které jsme vytvořili třídu Book v minulé lekci.
# Třída měla atributy title, pages and price. Nyní uvažujeme, že se nakladatelství rozhodlo vydávat i audioknihy.
# Ty nemají počet stránek, ale musíme u nich evidovat herce nebo herečku, který/která audioknihu předčítá.
# Budeme tedy chtít vytvořit třídu AudioBook, ale ta by neměla přímo dědit od třídy Book, protože by nám tam zbyl nepotřebný atribut pages.
# Musíme tedy prové úpravu již existujícího kódu. Takové úpravě se někdy říká refaktorizace.

# Vytvoř třídu Item, což je obecná položka, kterou bude nakladatelství prodávat. Třída Item bude mít atributy title a price.
# Uprav třídu Book tak, aby dědila od třídy Item. Třída Book bude mít navíc atribut pages.
# Atributy title a price nastav s využitím metody __init__ rodičovské třídy Item. Dále přidej třídu AudioBook,
# která bude mít navíc atributy duration_in_hours (délka nahrávky v hodinách) a narrator (člověk, který knihu čte).
# Třída AudioBook bude opět dědit od třídy Item a atributy title a price bude nastavovat s využitím metody __init__ rodičovské třídy Item.

# Třída Book si zachová svoji metodu get_time_to_read(), která pracuje s počtem stran (pages). Třída AudioBook bude mít metodu get_time_to_read()
# taky a při jejím zavolání bude vracet hodnotu atributu duration_in_hours. Pokud mají metodu všichni potomci, je běžné metodu přidat i rodičovské třídě.
# Přidej tedy metodu get_time_to_read() třídě Item. Do metody vlož klíčové slovo pass, protože pro třídu Item nebudeme do metody vkládat žádný výpočet.

# Vytvoř objekty reprezentující audioknihu Problém tří těles (délka 14.4, čte Zbyšek Horák, cena 299 Kč) a knihu Kadet Hornblower (242 stran, cena 399 Kč).
# Uvažuj, že nakladatelství přidá do e-shopu funkci, která vrátí celkový čas, kdy si bude moci zákazník nebo zákaznice užívat nakoupené produkty.
# Vytvoř tedy proměnnou total_time, která bude obsahovat součet délky audioknihy a času potřebného na přečtení knihy. Obojí zjisti s využitím metody get_time_to_read().

# Vlozka o importech ktera se nam ale v prikladu prilis nehodi
# Mohou byt i importy - 2 zpusoby
# from muj_modul import Book
# import muj_modul # pak se ale na tridu musim odkazovat jako muj_modul.Book

# Struktura trid
# Item
#   -> Book(Item)
#   -> Audiobook(Item)

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

# audiokniha = AudioBook('Problém tří těles', 299, 14.4, 'Zbyšek Horák')
# kniha = Book('Kadet Hornblower', 242, 399)
# total_time = kniha.get_time_to_read() + audiokniha.get_time_to_read()
# print(f'Budes potrebovat {total_time} h')