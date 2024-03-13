# Lehke opakovani
print('Hello world!')
textovy_typ = "Andy"
cislo = 20
desetinne_cislo = 20.5
seznam = [1, 2, 3, 4]


if cislo > 30:
    print('Je vetsi nez 30')
elif cislo > 10:
    print('je vetsi nez 10')
else:
    print('Neni vetsi nez 30')


for pismenko in textovy_typ:
    print(pismenko)


## Prvni cast - slicing

jmeno = "Spongebob Squarepants"
venecky_k_snidani = [2, 3, 4, 5, 6, 7]

print(jmeno[-1])
print(venecky_k_snidani[-2])
print(venecky_k_snidani[2:-2])

if 'A' in jmeno:
    print('Tvoje jmeno obsahuje "A"')

if 'A' not in jmeno:
    print('Tvoje jmeno neobsahuje "A"')


venecky_k_snidani[1] = 100
print(venecky_k_snidani)


## Druha cast - metody
# metody nad retezci - replace, split a dalsi https://docs.python.org/3/library/stdtypes.html#string-methods
# metody nad listy - treba append - https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

# len("jmeno")
# len([1,2,3])
# min()
# max()

divadelni_predstaveni = 'Romeo a Julie'

print(divadelni_predstaveni.upper())
print(divadelni_predstaveni.lower())

print(divadelni_predstaveni.split())
print(divadelni_predstaveni.split(" "))
print(divadelni_predstaveni.split("a"))
print(divadelni_predstaveni.split("x"))

print('/'.join(['a', 'b', 'c']))


print(divadelni_predstaveni.replace('Romeo', 'Honza'))

muj_list = [1,2,3]
muj_list.append(4)
print(muj_list)
