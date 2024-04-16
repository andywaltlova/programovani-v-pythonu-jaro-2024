# OOP a funkce - https://kodim.cz/czechitas/python-oop/lekce/dedicnost/dalsi-funkce
# Provazani objektu - https://kodim.cz/czechitas/python-oop/lekce/dedicnost/provazani-objektu

class Employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement

    def get_info(self):
        return f'Zaměstnanec {self.name} pracuje jako {self.position}.'

class Manager(Employee):

    def __init__(self, name, position, subordinates, car):
        super().__init__(name, position)
        self.holiday = 30
        self.subordinates = subordinates
        self.car = car

    def __str__(self):
        return super().__str__() + " a je to manazer"





# Cviceni

# Github - https://kodim.cz/czechitas/daweb/zaklady-gitu/uvod-do-gitu/system-git, https://github.com/

# Cviceni? - jen vyzkouseni s koucem, zalozeni repoziare
