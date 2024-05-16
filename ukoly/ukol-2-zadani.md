# Úkol 2 🐱 🐈

Tvojou úlohou bude napísať program, ktorý získa pomocou API 10 náhodných faktov o mačkách a uloží ich do súboru vo formáte JSON.

## Získavanie náhodných faktov

Keďže sme programátori, nebudeme náhodné fakty hľadať náhodne po internete a kopírovať ich do programu. Použijeme API, konkrétne endpoint [https://cat-fact.herokuapp.com/facts](https://cat-fact.herokuapp.com/facts). Ten vám ako odpoveď na request (dotaz) vráti objekt vo formáte JSON, v ktorom sa nachádza kľúč `text`, v ktorom sa nachádza náhodný fakt.

Dokumentace k endpointu se nachází na https://alexwohlbruck.github.io/cat-facts/docs/endpoints/facts.html, pomocí informací tam uvedených získej alespoň 10 faktů. Je to velice podobné tomu, jako když jsme na lekci získavali jména která slaví svátek pro daný den.

*Pozn. Nehledejte za tím něco extra složité, začněte stejně jako v [lekci na API a JSON na kodim](https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/json/json-api) :)*

## Filtrovanie faktov

Získané dáta obsahujú veľa ďalších informácií, ktoré sú pre nás zbytočné. Musíme si teda získať iba hodnoty, ktoré sú priradené kľúču `text`. Tieto hodnoty sú typu reťazec (string).

*Pozn. Pokud nevíš kde začít, začni s [lekcí na práci se slovníky na kodim](https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/slovniky/slovniky).*

## Vytvorenie zoznamu faktov

Po tom, ako vyfiltrujeme fakty, chceme si z nich vytvoriť zoznam, ktorý bude obsahovať všetky získané fakty. K reťazcom obsahujúcim fakty pridáme ešte ich očíslovanie, aby sme si boli istí, že ich máme presne 10.

*Pozn. Pokud nevíš kde začít, mrkni do minulého domácího úkolu jak si vytvářel/a seznamy zamestnancu a zvirat.*

## Vytvorenie súboru

Po vytvorení zoznamu nám ostáva už len posledný krok. Program vytvorí súbor `kocici_fakta.json`, do ktorého uloží náš zoznam s faktami. Aby sa nám zoznam lepšie čítal, pridáme do neho odsadenie (indent).

*Pozn. Pokud nevíš kde začít, začni s [lekcí na práci se soubory na kodim](https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/soubory/cteni-souboru).*

## Finálny súbor

Obsahu súboru by mal po prebehnutí programu vyzerať takto:

```json
[
    "1. Owning a cat can reduce the risk of stroke and heart attack by a third.",
    "2. Most cats are lactose intolerant, and milk can cause painful stomach cramps and diarrhea. It's best to forego the milk and just give your cat the standard: clean, cool drinking water.",
    "3. Domestic cats spend about 70 percent of the day sleeping and 15 percent of the day grooming.",
    "4. The frequency of a domestic cat's purr is the same at which muscles and bones repair themselves.",
    "5. Cats are the most popular pet in the United States: There are 88 million pet cats and 74 million dogs.",
    "6. Owning a cat can reduce the risk of stroke and heart attack by a third.",
    "7. Most cats are lactose intolerant, and milk can cause painful stomach cramps and diarrhea. It's best to forego the milk and just give your cat the standard: clean, cool drinking water.",
    "8. Domestic cats spend about 70 percent of the day sleeping and 15 percent of the day grooming.",
    "9. The frequency of a domestic cat's purr is the same at which muscles and bones repair themselves.",
    "10. Cats are the most popular pet in the United States: There are 88 million pet cats and 74 million dogs."
]
```

Jednotlivé fakty budú viac ako pravdepodobné iné (predsa len ide o náhodné fakty), ale vyzerať by to malo približne takto.

## Dotaz ešte raz

Náhodných faktov o mačkách nie je nikdy dosť. Preto si vypýtame ešte nejaké navyše. Keďže sme nedočkaví, nastavíme si `timeout` na 0.001, nech ich máme čo najrýchlejšie. Tu však môže nastať problém, že nám endpoint nestihne do tej doby odpovedať. Vtedy by nám spadol program s výnimkou balíčku `requests`, ktorá sa volá `Timeout`. Ako vieme, vyhodenie výnimky by nám zhodilo program, čo úplne nechceme. Preto napíšeme túto časť kódu tak, aby nám zachytil výnimku a namiesto nej len vypísal, že sme príliš nedočkaví.

### Poznámky

1. Poriadne sa pozri, ako vyzerá odpoveď (response) na dotaz (request). Pravdepodobne ti to zjednoduší prácu.
2. Skúste nechať spadnúť posledný dotaz (request), aby ste videli, ako vyzerá výnimka.
3. Trocha som v zadaní klamal. Ten posledný dotaz (request) vyhodí výnimku takmer vždy, pretože tisícina sekundy je príliš málo času na obdržanie odpovede (priemerne je rýchlosť odpovede niekde medzi 0.2 a 0.5 sekundy, môže byť pokojne aj dlhšie).

Dokumentace pro `requests` modul je [zde](https://requests.readthedocs.io/en/latest/user/quickstart/), je v něm možné najít příklad kódu který danou vyjímku vyhazuje.
