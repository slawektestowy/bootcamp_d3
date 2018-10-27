napis = input("Podaj napis: ").lower()
litery = dict()
for litera in napis:
    if litera in litery:
        litery[litera] += 1
    else:
        litery[litera] = 1
#print(litery)
for litera in litery:
    print(f"{litera}: {litery[litera]}")
