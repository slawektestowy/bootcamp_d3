def wiecej_niz(napis, ile_znakow):
    napis = napis.lower()
    zbior = set()
    wystapienia = {}
    for znak in napis:
        if znak in wystapienia:
            wystapienia[znak] += 1
        else:
            wystapienia[znak] = 1

    for literka in wystapienia:
        if wystapienia[literka] >= ile_znakow:
            zbior.add(literka)
    return zbior

    # for znak in napis:
    #     if napis.count(znak) >= ile_znakow:
    #         zbior.add(znak)
    # return zbior

    #return {znak for znak in napis if napis.count(znak) >= ile_znakow}

print(wiecej_niz("ala ma kota bbbbbb", 2))
