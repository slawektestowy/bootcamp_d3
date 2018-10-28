def policz_znak(napis, znak_poczatek='<', znak_koniec='>'):
    czy_liczymy = False
    napis = "bla<bla>bla"
    liczba = 0
    ile_nawiasow = 0

    for znak in napis:
        if znak == znak_poczatek:
            czy_liczymy = True 
            ile_nawiasow +=1
        elif znak == znak_koniec:
            czy_liczymy = False
            ile_nawiasow -=1
        elif czy_liczymy:
            liczba += ile_nawiasow
    return liczba
print(policz_znak("Ala ma <kota <a kot>> ma <ale>."))