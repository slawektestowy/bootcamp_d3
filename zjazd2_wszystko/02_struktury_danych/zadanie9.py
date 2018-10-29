ceny = {'marchewki': 1.99, 'ziemniaki': 0.98, 'bataty': 8.99}
magazyn = {'marchewki': 100.0, 'ziemniaki': 500.0, 'bataty': 10.0}

while True:
    print("Dostępne produkty:")
    for i in ceny:
        print(f'{i} Cena: {ceny[i]}/kg - {magazyn[i]}kg w magazynie.')
    print()

    akcja = input("Jaką akcje chcesz wykonać(KUP/DODAJ)? ")
    if akcja == 'KUP':
        produkt = input("Co chciałbyś kupić? ")
        if produkt in ceny:
            ile = float(input("Ile kg?"))
            if ile > magazyn[produkt]:
                print("Za dużo!")
            else:
                magazyn[produkt] -= ile
                naleznosc = ile * ceny[produkt]
                print(f"Za swoje zakupy płacisz {naleznosc:.2f} PLN.")
        else:
            print('Nie ma takiego produktu!')
    elif akcja == "DODAJ":
        co = input("Podaj produkt: ")
        cena = float(input("Cena: "))
        ile = float(input("Ile: "))
        ceny[co] = cena
        if co in magazyn:
            magazyn[co] += ile
        else:
            magazyn[co] = ile

