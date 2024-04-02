# Teorie - https://kodim.cz/czechitas/python-oop/lekce/tridy/tridy
# Proc OOP

zamestnanec_pomoci_listu = ['Jirka', 'Manazer', 25]
zamestnanec_pomoci_slovniku = {
    'name': 'Jirka',
    'position': 'Manazer',
    'holiday': 25
}

# def nazev_funkce(parametry):
#     pass
#     return 'nejaka hodnota'

# zamestnanec_pomoci_listu.append()


class Employee:
    def __init__(self, name, position, holiday=25):
        # magicke metody nebo dunder = double under
        # nejaky kod
        # self.nazev_atributu = "nejaka hodnota"
        self.name = name
        self.position = position
        self.holiday = holiday
        self.contract = "DPP"

    def __str__(self):
        return f"{self.name}({self.position}) - {self.holiday} dni dovolene."

    # Plus dalsi metody treba v oficialni dokumentaci - https://docs.python.org/3/reference/datamodel.html#special-method-names
    # a nebo na googlu :)
    def __eq__(self, druhy_objekt) -> bool:
        if isinstance(druhy_objekt, Employee):
            stejne_jmeno = self.name == druhy_objekt.name
            stejna_pozice = self.position == druhy_objekt.position
            stejna_dovolena = self.holiday == druhy_objekt.holiday
            return stejna_pozice and stejne_jmeno and stejna_dovolena
        else:
            return False

    # Co se stane kdyz budu mit dve definice
    # def __str__(self):
    #     return f"{self.name}({self.position}) - {self.holiday} dni dovolene. :)"

    def get_info(self):
        # f-string (formatovany retezec)
        # return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
        return "Zaměstnanec " + self.name + " pracuje na pozici " + self.position + "."

    def take_holiday(self, days: int):
        # self.holiday = self.holiday - days
        if self.holiday >= days:
            self.holiday -= days
            return f'{self.name} si bere {days} dni dovolene.'
        else:
            return f'Nemas narok na {days} dni, mas k dispozici pouze {self.holiday}.'


kouc_1 = Employee("Martin", "Senior kouc", 0)
kouc_2 = Employee("Martin", "Senior kouc", 0)

lektor = Employee("Jirka", 'Senior lektor')

print(kouc_1)
print(kouc_2)
print(kouc_1 == kouc_2)
print(kouc_1 == "retezec")




