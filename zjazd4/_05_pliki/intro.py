import os

f = open('jakiś_plik.txt','w')
print('po otwarciu recznym',f.closed)
f.write("ala ma kota")
f.close()
print('po zamknieciu recznym',f.closed)

with open('plik.txt','w') as f:
    print('po otwarciu za pomocą with', f.closed)
    ile = f.write('kot ma ale\na pies ma ole')
    print(f'zapisalem {ile} znaków do pliku')
print('po wyjciu z with',f.closed)

# w - write (nadpisuje plik)
# r - read (domyślnie)
# a - append
# r+ - read/write
# wb, rb, ab, rb+ - binary

with open('plik.txt','r') as f:
    dane = f.read() # czyta cały plik do końca
    print('cała zawartość pliku:',dane, sep='\n', end='\n')

with open('plik.txt','r+') as f:
    dane = f.readline() # czyta 1 linię
    print('pierwsza linia:\n',dane)
    dane = f.read(4) # czyta zadaną liczbę znaków
    print('pierwsze 4 znaki drugiej linii:', dane)
    f.seek(5)   # ustawia kursor przed 6 znakiem
    dane = f.read(4)
    print('znaki od 6 wzwyż:', dane)

    # to działa dla odczytu binarnego
    # f.seek(-5,2)    # 2gi arg: 0 - poczatek, 1 - aktualna pozycja, 2 - koniec

    # obejcie problemu dla odczytu tekstowego
    f.seek(0, os.SEEK_END)  # przesun sie na koniec pliku; f.seek(0, 2) is legal
    poz = f.tell() # zczytaj pozycję za pomocą tell()
    f.seek(poz - 5, os.SEEK_SET)   # przesun sie na poz-5 od poczatku pliku

    dane = f.read(3)
    print(dane)

with open('plik.txt','r') as f:
    linie = f.readlines()
    print(linie)