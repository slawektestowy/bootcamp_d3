# Napisz program wczytujacy plik z logami aktywnosci uzytkowników
#
# w systemie. Na podstawie wczytanych danych wyswietl informacje o
#
# sumarycznym czasie przebywania kazdego uzytkownika w systemie.
#
# Przykład uzycia:
#
# $ python read_logs.py logs.txt
#
# Czas przebywania w systemie:
#
# - user-1: 92 s
#
# - user-2: 51 s               LOGS.TXT
#
# - user-3: 20 s

#
#  otowrzyc plik   read
# czytamy linia po linii ( readlines() )
# dzielimy za pomoca split
# robimy slownik (user:czas)  (dodajemy logouty, odejmujemy login)

with open('logs.txt','r') as f:
   suma_czasow = dict()
   for linia in f.readlines():
       user, akcja, czas = linia.split(';')
       czas = int(czas)
       if akcja == "LOGIN":
           if user in suma_czasow:
               suma_czasow[user] -= czas
           else:
               suma_czasow[user] = -czas
       else:
           suma_czasow[user] += czas

for linia in suma_czasow:
    print(f'{linia}:{suma_czasow[linia]}')