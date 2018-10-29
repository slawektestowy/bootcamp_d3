lista = [i / 10 for i in range(11)]
print(lista)
zbior = {(i, i ** 2, i ** 3) for i in range(-10, 11)}
print(zbior)
napisy = {'Ala' * i for i in range(1,5)} | {"mewa" * i for i in range(1,4)}
slownik = {napis : len(napis) for napis in napisy}
print(slownik)
