# OOP a funkce - https://kodim.cz/czechitas/python-oop/lekce/dedicnost/dalsi-funkce
# Provazani objektu - https://kodim.cz/czechitas/python-oop/lekce/dedicnost/provazani-objektu

class Employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement

    def __str__(self):
        return f'Zaměstnanec {self.name} pracuje jako {self.position}.'

class Manager(Employee):
    def __init__(self, name, position, subordinates: list, car):
        super().__init__(name, position, 30)
        self.subordinates = subordinates
        self.car = car

    def __str__(self):
        return super().__str__() + " [Manazer]"

class Brigadnik(Employee):
    def __init__(self, name, position):
        super().__init__(name, position, 0)

    def __str__(self):
        return super().__str__() + " [Brigadnik]"

class Salesman(Employee):
    def __init__(self, name, position, holiday_entitlement, car):
        super().__init__(name, position, holiday_entitlement)
        self.car = car

    def __str__(self):
        return super().__str__() + " [Brigadnik]"


# Podrizeni
karolina = Employee('Karolina', 'Prodavacka zmrzliny', 0)
adolf = Brigadnik('Adolf', 'Ridic tramvaje')
ruzenka = Salesman('Ruzenka', 'Prodavacka pracich prasku', 25, 'Ford')

# Manager
podrizeni = [karolina, adolf, ruzenka]
karel = Manager('Karel', 'Prodavac kafe na hlavnim nadrazi', podrizeni, 'Skoda')

for podrizeny in karel.subordinates:
    print(isinstance(podrizeny, Employee))
    print(podrizeny.holiday_entitlement)

# Cviceni

# Github - https://kodim.cz/czechitas/daweb/zaklady-gitu/uvod-do-gitu/system-git, https://github.com/



