licznik = 0
for liczba in range(101):
    if liczba % 3 == 0 or liczba % 5 == 0:
        print(liczba)
        licznik += 1
print(f'znalazlam {licznik} liczb podzielnych przez 3 lub 5')

# if not ((liczba % 3) * (liczba % 5)) :