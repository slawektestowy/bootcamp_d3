# Napisz program sprawdzajacy, czy podana przez uzytkownika liczba
# jest:
# a) wieksza od 10
# b) mniejsza równa 15
# c) podzielna przez 2 (uzyj operatora modulo % - reszta z dzielenia)

# Przykładowy komunikat programu:
# Podaj liczbe: 15
# Wieksza od 10: True
# Mniejsza równa 15: True
# Podzielna przez 2: False

x=3
if x == 1:
    print('pierwsza ścieżka wykonania')
elif x == 2:
    print('druga, alternatywna ściezka wykonania')
else:
    print('ostatnia deska ratunku')

#komunikacja z człowiekiem
if x >10:
    print('liczba większa niż 10')
else:
    print('liczba mniejsza równa niż 10')

#komunikacja z maszyną/programem
x = int(input('podaj liczbę:'))
print('Czy liczba większa niż 10:', x>10)
print('Czy liczba mniejsza niż 15:', x<15)
print('Czy liczba podzielna przez 2:', x % 2 == 0)
print('Czy liczba podzielna przez 2:', not bool(x % 2))


print( x>2 and x<6)
print( x >= 0 or x < -100)
print( 1==1 and 2==3 or 4>2)