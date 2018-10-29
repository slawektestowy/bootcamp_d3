# zad2
#
a = 3
b = 9
h = 6.5

pole = (a + b) * h / 2
# f-stringi pozwalają na szybkie formatowanie liczb
# od pythona 3.6
print(f'Wynik {pole} cm2')
print(f'Wynik {(a+b)*h/2:.2f}')

# w starszych pythonach
print('Wynik', pole, 'cm2')

# zad3

imie = 'Agata'
wzrost = 170

print(f'imie: {imie} \n'
      f'wzrost: {wzrost}')

print(f'imie: {imie} \nwzrost: {wzrost}')

print(f'''imie: {imie}
wzrost: {wzrost}''')

print(f'imie: {imie}', f'wzrost: {wzrost}', sep='\n')
print(f'imie: {imie}', f'wzrost: {wzrost}', 'waga', 4, sep='^^^')

# zad4
cena = 30
waga = 2.5
koszt = cena * waga

print(f'Cena towaru: {cena}\n'
      f'Waga: {waga}\n'
      f'Koszt: {koszt}')

# input
#
# imie = input('podaj napis:')
# print(imie)
# z = int(input('wpisz liczbę: '))
# print(z)

# zad5

# tzw CamelCase
miastoPierwsze = ''
miastoDrugie = ''

# zamiast spacji znaki podkreślenia
miasto_a = ''
miasto_b = ''

# blokowe komentarze
# CTRL + /

m1 = input('Miasto A: ')
m2 = input('Miasto B: ')
dys = float(input(f'Dystans {m1}-{m2}: '))
cena = float(input('Cena paliwa: '))
sp = float(input('Spalanie na 100km: '))

print(f'Koszt przejazdu {m1}-{m2} '
      f'to {dys/100*cena*sp:.2f}PLN')

# if
x = 7
if x > 5:
    print('duża liczba')

if x > 5:
    print('duża liczba')
else:
    print('mała liczba')

if x > 5:
    print('duża')
    print('druga linia')
    print('trzecia')
elif x > 3:
    print('średnia')
else:
    print('mała')
