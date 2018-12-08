# Napisz program obsługujacy baze danych pracowników. W bazie
# danych przechowuj imie, nazwisko, email, rok urodzenia, pensje.
# Skorzystaj z modułu json.
# Przykład uzycia:
# $ python employees.py
# Co chcesz zrobic? [d - dodaj, w - wypisz] d
# Imie: Jan
# Nazwisko: Nowak
# Rok urodzenia: 1980
# Pensja: 5000.0
# $ python employees.py
# Co chcesz zrobic? [d - dodaj, w - wypisz] w
# Pracownicy:
# - [1] Jan Nowak - rok: 1980, pensja: 5000.00 PLN
# Materiał chroniony
import json

try:
    with open('baza_pracownikow.json','r') as file:
        pracownicy = json.load(file)
except FileNotFoundError:
    pracownicy = []

while True:
    akcja = input('Co chcesz zrobic? [d - dodaj, w - wypisz, s - skasuj, z - zakończ]')

    if akcja.lower() == 'z':
        # zapisz bazę i wyjdź
        with open('baza_pracownikow.json', 'w') as file:
            json.dump(pracownicy,file)
        break

    if akcja.lower() == 'w':
        # wypisz razem z numerkami
        for nr,prac in enumerate(pracownicy):
            print(f'[{nr+1}] {prac["imie"]} {prac["nazwisko"]}: '
                  f'Rok urodzenia: {prac["rok_urodzenia"]}, '
                  f'Pensja: {prac["pensja"]:.2f}PLN')

    if akcja == 's':
        nr = int(input('podaj nr pracownika do skasowania: '))
        pracownicy.remove(pracownicy[nr-1])

    if akcja.lower() == 'd':
        imie = input('podaj imię: ')
        nazwisko = input('podaj nazwisko: ')
        rok_urodzenia = input('podaj rok urodzenia: ')
        pensja = float(input('podaj pensję: '))
        pracownicy.append({'imie':imie,
                           'nazwisko':nazwisko,
                           'rok_urodzenia':rok_urodzenia,
                           'pensja':pensja})

