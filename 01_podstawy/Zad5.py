miastoa = input('podaj pierwsze miasto: ')
miastob = input('podaj drugie miasto: ')
Dystans = float(input('podaj odleglosc: '))
Cena = float(input('podaj cene paliwa: '))
Spalanie = float(input('podaj spalanie na 100km: '))
Koszt = Dystans/100*Spalanie*Cena
print(f'Miasto A: {miastoa}', f'Miasto B: {miastob}',
      f'Dystans {miastoa}-{miastob}: {Dystans}',
      f'Cena paliwa: {Cena}',
      f'Spalanie na 100km: {Spalanie}','\n',
      f'Koszt przejazdu {miastoa}-{miastob} to {Koszt:.2f} PLN', sep='\n')
