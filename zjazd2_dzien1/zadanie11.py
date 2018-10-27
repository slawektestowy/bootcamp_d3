zbior = set()
while True:
    napis = input("Podaj liczbe lub 'k' zeby zakonczyc: ")
    if napis == 'k':
        break
    liczba = int(napis)
    zbior.add(liczba)
print(zbior)
print(f"Unikalnych liczb: {len(zbior)}")
parzyste = set(range(0,101,2))
print(parzyste)

print(zbior & parzyste)
