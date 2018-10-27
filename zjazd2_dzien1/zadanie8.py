napis = input("Podaj napis: ")
ile_znakow = 0
czy_liczymy = False

for znak in napis:
    if znak == '<':
        czy_liczymy = True
    elif znak == '>':
        czy_liczymy = False
    elif czy_liczymy:
        ile_znakow += 1

print(ile_znakow)