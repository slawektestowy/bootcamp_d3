from math import sqrt

def czy_podzielne_przez_7(x):
    if x % 7 == 0:
        return True
    else:
        return False

def czy_pierwsza(x):
    if x == 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


print(czy_pierwsza(17))
print(czy_pierwsza(25))
print(sqrt(5))
print(sqrt(25))