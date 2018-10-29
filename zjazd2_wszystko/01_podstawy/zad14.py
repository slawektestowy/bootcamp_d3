# komenda końcowa: stop
# jeśli użytkownik skończy nie podając żadnej liczby
# wypisujemy "brak danych"

# 3 zmienne do przechowywania danych
# min_l = 0
# max_l = 0
# akt_l

odp = input('wpisz liczbę lub "stop": ')
if odp.strip("'").lower() == 'stop':
    print('brak danych')
else:
    akt_liczba = int(odp)
    min_liczba = akt_liczba
    max_liczba = akt_liczba

    while odp.strip("'").lower() != 'stop':

        # tu jest miejsce na obsługę
        # tego co użytkownik nam dał
        akt_liczba = int(odp)
        if akt_liczba > max_liczba:
            max_liczba = akt_liczba

        if akt_liczba < min_liczba:
            min_liczba = akt_liczba

        odp = input('wpisz liczbę lub "stop": ')

    print(f'''największa znaleziona: {max_liczba}
    najmniejsza znaleziona: {min_liczba}''')

    print(f'największa znaleziona: {max_liczba}\n'
          f'najmniejsza znaleziona: {min_liczba}')

    print(f'największa znaleziona: {max_liczba}'
          , f'najmniejsza znaleziona: {min_liczba}'
          , sep='\n')

    print(f'największa znaleziona: {max_liczba}')
    print(f'najmniejsza znaleziona: {min_liczba}')
