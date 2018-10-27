a = 3
b = 9
h = 6.5
p = (a+b)*h/2
print("oblliczenia pola trapezu")
print(f'Wynik: {p}cm2')


i = "Michal"
w = 177
print(f"""Imie: {i}
Wzrost: {w}cm""")
print (f'Imie: {i}', f'Wzrost: {w}', sep='\n')


cena = 10
waga = 2.5
naleznosc = cena*waga

print(f'Cena za kg: {cena}', f'Waga: {waga}', f'Naleznosc: {naleznosc}', sep='\n')


#INPUT

x = input('podaj swoj wiek')
jesli input ma byc liczba to nastepnie trzeba podac
int(x) wtedy jest to interpretowane jako liczba to co sie wklepie po zapytaniu

x = int(input('wpisz wiek'))


MiastoA = input('podaj pierwsze miasto')
MiastoB = input('podaj drugie miasto')
Dystans = int(input('podaj odleglosc'))
Cena = float(input('podaj cene paliwa'))
Spalanie = float(input('podaj spalanie na 100km'))
Koszt = Dystans/Spalanie*Cena
print(f'Miasto A: {MiastoA}', f'Miasto B: {MiastoB}', f'Dystans {MiastoA}-{MiastoB}: {Dystans}', f'Cena paliwa: {Cena}', f'Spalanie na 100km: {Spalanie}','\n', f'Koszt przejazdu {MiastoA}-{MiastoB} to {Koszt} PLN', sep='\n')
