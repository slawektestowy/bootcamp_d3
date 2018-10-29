def policz_znak(napis, znak_poczatek='<', znak_koniec='>'):
    ile_znakow = 0
    ile_nawiasow = 0
    for znak in napis:
        if znak == znak_poczatek:
            ile_nawiasow += 1
        elif znak == znak_koniec:
            ile_nawiasow -= 1
        else:
            ile_znakow += ile_nawiasow
    return ile_znakow

print(policz_znak("Ala ma <kota> i psa."))
print(policz_znak("Ala ma <kota <a kot>> ma <ale>."))
print(policz_znak('a <a<a<a>>>'))
