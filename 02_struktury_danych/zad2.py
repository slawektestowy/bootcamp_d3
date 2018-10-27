lista = []

while len(lista) < 10:
    lista.append(int(input('podaj liczbe: ')))

print(lista)
wynik = sum(lista)
print(wynik/len(lista))

