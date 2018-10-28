from math import sqrt
def funkcja():
    print("No elo")


# def czesc(imie):
#     print(f"Czesc {imie}")
# #
# print("Czesc  Katarzyna")
# print("Czesc Zenon")

#funkcja()
# czesc("Katrzyna")
# czesc("Zenon")


# def czesc(imie, imie2):
#     print(f"Czesc {imie} i {imie2}")
#
# czesc("Kasia", "Henio")
print(sqrt(25))

# def kwadrat(x):
#     wynik = x**2
#     return wynik
#
#
# x = kwadrat(7)
# print(x)
# print([kwadrat(i) for i in range(10)])

# def czy_jest_pierwsza(x):
#     if x%2 == 0 and x == 2:
#         print("Liczba jest liczba pierwsza")
#     elif x%2 !=0:
#         print("Liczba jest liczba pierwsza")
#
#     else:
#         print("Liczba nie jest liczba pierwsza")
#     return
#
# czy_jest_pierwsza(9)

# def czy_pierwsza(x):
#     dzielnikow = 0
#     for i in range(1, x+1):
#         if x % i == 0:
#             print(f"{x} jest podzielna przez {i}")
#             dzielnikow +=1
#         if dzielnikow ==2:
#             return True
#         return False
#
# print(czy_pierwsza(10))


def pierwsza(x):
    if x ==1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

print(pierwsza(10))
sqrt(25)