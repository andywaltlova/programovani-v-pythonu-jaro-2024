# https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/json/format-json


import json

with open("absolvetni.json", encoding="utf-8") as file:
    absolvents = json.load(file)
print(absolvents)


hours = {'po': 8, 'ut': 7, 'st': 6, 'ct': 7, 'pa': 8}
with open("nieco.json", mode='w', encoding="utf-8") as output_file:
    json.dump(hours, output_file)


# https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/json/json-api
