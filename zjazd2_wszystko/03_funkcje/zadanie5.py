def silnia(x):
    if x == 0:
        return 1
    return x * silnia(x - 1)
    
    # wynik = 1
    # for i in range(1, x + 1):
    #     wynik *= i
    # return wynik

print(silnia(5))