x = int(input('Podaj pierwsza liczbe: '))
y = int(input('Podaj druga liczbe: '))


if 0 <= x <= 10:
    if 0 <= y <= 10:
        print('lewy gorny')
    elif 0 < y <90:
        print('lewy')
    elif 90 <= y <= 100:
        print('lewy dolny')
    else:
        print('jestes poza plansza')
elif 10 < x <90:
    if 0 <= y <= 10:
        print('gora')
    elif 0 < y <90:
        print('srodek')
    elif 90 <= y <= 100:
        print('dol')
    else:
        print('jestes poza plansza')
elif 90 <= x <= 100:
    if 0 <= y <= 10:
        print('prawy gorny')
    elif 0 < y <90:
        print('prawy')
    elif 90 <= y <= 100:
        print('prawy dolny')
    else:
        print('jestes poza plansza')
else:
    print('jestes poza plansza')