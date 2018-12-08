# Napisz program wczytujacy liste adresów email z pliku i tworzacy
# nowy plik z odfiltrowana zawartoscia.
# Wejsciowy plik moze zawierac duplikaty adresów, ten sam adres
# pisany rózna wielkoscia liter, linie zawierajace białe znaki oraz
# błedne adresy email (brak znaku @ lub wystepuje on wiele razy).
# Wynikowy plik powinien zawierac unikalne, posortowane, poprawne
# adresy email.
# Przykład uzycia:
# $ python clean_emails.py emails.txt cleaned_emails.txt

# 1. otwieramy plik (read)
# 2. wczytujemy linie
    # spradzamy małpy -> jeśli źle to nastepna linia

    # podziel i sprawdz długość powstałej listy
    # if len(linia.split(';')) != 2:

    # policz ile jest znaków podziału
    # if 'ala ma kota  '.count(' ') != 1:
    #     continue
    # 'ala m akota  '.lower().strip()
    # wrzuć do zbioru
# 3. otworz nowy plik (write)
#     zapisz do pliku ten zbior
emails = set()
with open('emails.txt','r') as f:
    for linia in f.readlines():
        if linia.count('@')!=1:
            continue
        emails.add(linia.lower().strip().replace(' ',''))

lista = list(emails)
lista.sort()
tresc = '\n'.join(lista)
with open('cleaned_emails.csv','r+') as f:
    f.write(tresc)
    f.seek(0)
    print(f.read())

