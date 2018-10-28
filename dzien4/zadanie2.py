def zbior_znakow(napis, ile_znakow):
    napis = napis.lower()
    zbior = set()

    for znak in napis:
         if napis.count(znak) >= ile_znakow:
             zbior.add(znak)
    return zbior
print(zbior_znakow("ala ma kota aaaaaa",3))


#     wystapienia = {}
#     for znak in napis:
#         if znak in wystapienia:
#             wystapienia[znak] +=1
#         else:
#             wystapienia[znak] = 1
#         return wystapienia
# print(zbior_znakow("ala ma kota",3))

    # napis = ("ala ma kota a kot ma ale")
    # zliczanie =








   # samogloski = "aeiouy"

    # for litera in napis:
    #     if litera in napis:
    #         ile_ile_znakow += 1
    #
    # print(f"W napisie '{napis}' jest {ile_samoglosek} samogłosek.")
