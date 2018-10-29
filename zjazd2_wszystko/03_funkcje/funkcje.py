def funkcja():
    print("No elo")

def czesc(imie, imie2='Janek'):
    print(f"Cześć {imie} i {imie2}")

def kwadrat(x):
    return x ** 2

czesc("Katarzyna", "Zenon")
czesc("Zenon")
funkcja()
x = kwadrat(7)
print(x)
print([kwadrat(i) for i in range(10)])