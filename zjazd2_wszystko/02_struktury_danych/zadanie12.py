lista = [2, 1, 4, 9, 3, 7]
# 1. Znajdź pozycję najmniejszego elementu w tablicy
for indeks_podstawienia in range(len(lista)):
    print(f'Przed zamianą: {lista}')
    min_index = None
    # for i in range(indeks_podstawienia, len(lista)):
    for i, liczba in enumerate(lista[indeks_podstawienia:], indeks_podstawienia):
        if min_index is None or liczba < lista[min_index]:
            min_index = i
    if min_index is None:
        break
    # 2. Zamień miejscami elementy
    lista[min_index], lista[indeks_podstawienia] = lista[indeks_podstawienia], lista[min_index]
    print(f'Po zamianie: {lista}')
print(f'Po sortowaniu: {lista}')