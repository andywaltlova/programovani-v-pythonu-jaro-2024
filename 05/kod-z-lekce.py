# Funkce
# Tridy
# Promenne - promenne uvnitr funkci, samotne promenne (plati v ruznych scope)
# Klasicky kod kery nepatri ani do funkce ani do tridy
# importy


# 1. Importy nahore
#    KONSTANTY, globalni promenne
# 2. Tridy , Funkce
# 3. Klasicky kod - volani funkci, vytvareni objektu ze trid ...

from dataclasses import dataclass

# Tridy - pripomenuti

# class Employee:
#     def __init__(self, name, position, holiday=25):
#         self.name = name
#         self.position = position
#         self.holiday = holiday

#     def __str__(self):
#         return f"{self.name} ({self.position}) - {self.holiday} holiday"

#     def take_holiday(self, days: int):
#         # self.holiday = self.holiday - days
#         if self.holiday >= days:
#             self.holiday -= days
#             return f'{self.name} si bere {days} dni dovolene.'
#         else:
#             return f'Nemas narok na {days} dni, mas k dispozici pouze {self.holiday}.'


# https://docs.python.org/3/library/dataclasses.html
@dataclass
class Employee:
    name: str
    position: str
    holiday: int = 25

    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.holiday_entitlement} dní."

    def __str__(self):
        return f"{self.name} pracuje na pozici {self.position}."

# Dedicnost - https://kodim.cz/czechitas/python-oop/lekce/dedicnost/dedicnost

@dataclass
class Manager(Employee):
    car: str = "nespecifikovano"
    holiday: int = 30

    # def __init__(self, name, position):
    #     super().__init__(name, position)
    #     self.holiday = 30
    #     self.podrizeni = ['Anna', 'Honza']

    def __str__(self):
        return super().__str__() + " a je to manazer"

# Klasicky kod

hanka = Manager("Hanka", "manazerka")
print(hanka)


from dataclasses import dataclass

@dataclass
class Superhero:
    name: str
    superpower: str
    energy: int = 100

    # def __init__(self, name: str, superpower: str):
    #     self.name = name
    #     self.superpower = superpower
    #     self.energy = 100  # Initial energy level

    def use_power(self):
        if self.energy >= 20:
            self.energy -= 20
            return f"{self.name} uses {self.superpower}! Energy decreased by 20."
        else:
            return f"{self.name} is too exhausted to use {self.superpower}."

    def rest(self):
        if self.energy < 100:
            self.energy += 20
            return f"{self.name} is resting. Energy increased by 20."
        else:
            return f"{self.name} is already fully charged!"

    def recharge(self):
        self.energy = 100
        return f"{self.name} is fully recharged and ready to save the day!"

hero = Superhero("Captain Python", "Pythonic Powers")
# print(hero.energy)






