def splaszcz(x):
    wynik = []
    for i in x:
        if isinstance(i, list):
            for k in splaszcz(i):
                wynik.append(k)
        else:
            wynik.append(i)
    return wynik
print(splaszcz([1, 2, 3, [4, 5, [6]], 7]))
