#komenda koncowa stop
#jesli uzytkownik nie poda zadnej liczby - brak danych


#min_1 = 0
#max_1 = 0
#akt_1
odp = input('wpisz liczbe lub "stop"')
if odp.strip('"') == 'stop':
    print('brak danych')
    exit()
else:
    min_1 = int(odp)
    max_1 = int(odp)
    while odp != 'stop':

        akt_1 = int(odp)

        if akt_1 > max_1:
           max_1 = akt_1

        if akt_1 < min_1:
           min_1 = akt_1

        odp = input('wpisz liczbe lub "stop"')
    else:
        print(min_1, max_1)