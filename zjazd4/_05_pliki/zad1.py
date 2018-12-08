# Napisz program wypisujacy na konsole zawartosc wskazanego pliku
# wraz z numerami linii. Obsłuz sytuacje, gdy uzytkownik nie poda
# nazwy pliku lub poda błedna nazwe.
# Przykład uzycia:
# $ python test.txt
# 1: pierwsza linia pliku
# 2: druga linia pliku

# 1. otworz plik, do odczytu
# 2. w petli czytaj po 1 linii i od razu wypisuj
#     - potrzebuje jakiego licznika
#     - kiedy petla sie skonczy?

# for licznik, wartosc in enumerate(lista):
# with open('plik.txt','r') as f:
    # to działa:
    # linia = f.readline()
    # while linia:
    #     linia = f.readline()
    #     print(f'{linia}')

# to jest bardziej po pythonowemu
with open('plik.txt', 'r') as f:
    i = 1
    while True:
        linia = f.readline()
        if not linia:
            break
        print(f'{i}:{linia}', end='')
        i+=1

#   za pomocą enumerate
with open('plik.txt','r') as f:
    lista = f.readlines()
    for x,wart in enumerate(lista):
        print(f'{x+1}: {wart}', end='')

# jeszcze raz to samo
with open('pusty.txt','r') as f:
    for x,wart in enumerate(f.readlines()):
        print(f'{x+1}: {wart}', end='')

