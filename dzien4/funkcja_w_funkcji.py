def wywolaj_funkcje(f, x):
    return f(x)

def fun(x):
    return x ** 2 + 1

fun2 = lambda x: x**3

print(wywolaj_funkcje(lambda x: -2*x, 2))
print(wywolaj_funkcje(fun2, 2))


def przycinka(lista, start, stop):
    wynik = []

    return wynik

def czy_wieksze_od_3(x):
    return x > 3

dane = [1,2,3,4,5,6,7,8]
print(przycinka(dane, czy_wieksze_od_3, lambda x:x ==6))

