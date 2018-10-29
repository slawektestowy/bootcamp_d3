def przytnij(lista, start, stop):
    wynik = []
    czy_liczymy = False
    for x in lista:
        if not czy_liczymy and start(x):
            czy_liczymy = True
        if czy_liczymy:
            wynik.append(x)
            if stop(x):
                break
    return wynik

def czy_wieksze_od_3(x):
    return x > 3

dane = [1,2,3,1,5,7,1,8,6,3,5]
print(przytnij(dane, czy_wieksze_od_3, lambda x : x == 1))