licznik=0
for liczba in range(101):
    if liczba % 3 == 0 or liczba % 5 == 0:
        print(liczba)
        licznik += 1
print(licznik)
