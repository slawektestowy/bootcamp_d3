from random import randint

liczba = randint(0, 100)

x = None
while x is None or x != liczba:
    x = int(input("Zgadnij jaka liczba: "))

    if x > liczba:
        print("Za dużo!")
    elif x < liczba:
        print("Za mało")
print("Brawo!")