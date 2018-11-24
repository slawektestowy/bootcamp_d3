f = open('jakis_plik.txt', 'w')   # nazwa pliku i tryb otwarcia
print('po otwarciu recznym', f.closed)
f.write('ala ma kota')  # zapisujemy cos dd pliku
f.close()  # musimy zamknac plik
print('po zamknieciu recznym', f.closed)


with open ('plik.txt','w') as f:
    print('po otwarciu za pomoca with', f.closed)
    f.write("kot ma ale\na pies ma ole")
print('po wyjsciu z with,', f.closed)


# w -write (nadpisuje plik)
# r - read (domyślnie)
# a append
# r+ read/write
# b - binary

with open('plik.txt','r') as f:
    dane = f.read() # czyta do konca
    print(dane)

with open('plik.txt', 'r') as f:
    dane = f.readline()  # czyta 1 linie
    print('pierwsza linia:',dane, sep='\n', end='\n')
    dane = f.read(4)  #czyta zadana liczbe znakow
    print ('pierwsze 4 znaki drugiej linii:', dane)
    f.seek(5) # ustawia kursor przed 6 znakiem
    dane = f.read(4)
    print('znaki od 6 wzwyz:', dane)
    # f.seek(-3,2) # 0 -poczatek, 1 -aktualna pozycja, 2 -koniec
    # dane = f.read(3)
    # print(dane)

with open('plik.txt','r') as f:
    linie = f.readlines()
    print(linie[0])