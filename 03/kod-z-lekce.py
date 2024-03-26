# https://kodim.cz/programovani/uvod-do-progr-2/uvod-do-programovani-2/slovniky/slovniky)
# https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/slovniky/slovniky-a-cykly

# Slovniky

konvicka = ["Čajová konvička s hrnky", 899, True]

# if 899 in konvicka:
#     print('Seznam obsahuje cenu')


# print(item[0])

konvicka = {
    "name": "Čajová konvička s hrnky",
    "price": 899,
    "in_stock": True,
}

# Ziskani hodnoty
# print(konvicka["name"])

# Ziskani s vychozi hodnotou
# print(konvicka.get("neexistujici", "Klic nenalezen"))

# Pridani hodnoty
konvicka["novy_klic"] = "nova_hodnota"

# Uprava hodnoty
konvicka["name"] = "Cajova konvicka s talirky"
konvicka["price"] = 1099
konvicka["price"] += 200

# Odebrani hodnoty
odebrana_hodnota = konvicka.pop("name")

# Odebrani s vychozi hodnotou aby nenastal KeyError
odebrana_hodnota = konvicka.pop("neexistujici", -1)

# print(odebrana_hodnota)
# print(konvicka)

# Pristupovani k hodnote klice ve slovniku
# print(item["name"])

# print(item["neexistujici"])


# Overeni ze klic je ve slovniku
# if "price" in konvicka:
#     # Neco se stane
#     print('Klic je ve slovniku')
# else:
#     print('Klic neni ve slovniku')


konvicka = {
    "id": 1,
    "name": "Čajová konvička s hrnky",
    # klic: hodnota
    "price": 899,
    "in_stock": True,
}

talirek = {
        "name": "Talirek",
        "price": 569,
        "in_stock": False,
}

eshop = [
    konvicka,
    talirek
]

def inflace(cena):
    return cena + 200

for item in eshop:
    item['price'] = inflace(item['price'])

    # nova_hodnota = inflace(item['price'])
    # item['price'] = nova_hodnota

# print(eshop)

# Rozdily mezi slovnikem a listem
# - list - serazeny
# - slovnik - na poradi nezalezi
# - list - k prvkum pristupujeme pomoci indexu
# - slovnik - k prvkum pristupujeme pomoci klice (at uz je to stirng nebo cislo nebo neco jineho)


# Realny priklad - slovnik popisujici dopravni prostredek na https://mapa.idsjmk.cz/
data = {
    "LastUpdate": "2024-03-26T17:38:19.5441399+01:00",
    "Vehicles": [
        {
            "ID": 30284,
            "IDB": 0,
            "IDC": 0,
            "VType": 5,
            "LType": 5,
            "Lat": 49.191032,
            "Lng": 16.613216,
            "Bearing": 0,
            "LineID": 135,
            "LineName": "R13",
            "RouteID": 806,
            "ServiceId": 13504,
            "Course": "13504",
            "LF": True,
            "Delay": 0,
            "LastStopID": 1146,
            "FinalStopID": 1146,
            "FinalStopName": "Hlavní nádraží",
            "IsInactive": False,
        },
        # ....
    ]
}






# Slovniky a cykly
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

# Vice rozepsane
hodnoty_slovniku = sales.values()
hodnoty_slovniku_na_list = list(hodnoty_slovniku)
# print(hodnoty_slovniku_na_list)

# Structnejsi zapis
# print(list(sales.keys()))


print(sales.items())

for klic, hodnota in sales.items():
    # print(klic, hodnota)
    if hodnota == 5681:
        print(klic)


# items()
# values()
# keys()

print(len(sales))
print('Pocet vsech prodanych knih', sum(sales.values()))


# seznam = [1,2,3]

# for polozka in seznam:
#     print(polozka)

# for polozka in sales:
#     print(polozka)


# if 5681 in sales.values():
#     print('Hodnota se nachazi v hodnotach slovniku')



