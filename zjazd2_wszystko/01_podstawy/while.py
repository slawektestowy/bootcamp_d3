# print(1)
# print(2)
# print(3)

# while warunek kontunuacji:
#     blok instrukcji
#
# 1. przygotowanie zmiennej sterującej
# 2. zdefiniowanie warunku kontynuacji
# 3. blok instrukcji
# 4. wewnątrz bloku istrucji zmieniamy zmienną sterującą


i = 0
while i<10:
    print(i)
    i = i+1

print('po pętli')

# petla nieskonczona
# while True:
#     cokolwiek

i+=1

# nieparzyste od 1 do 100
i=1
while i<100:
    print(i)
    i+=2
print('po pelti')

# liczby od 100 do 1
i=100
while i>0:
    print(i)
    i-=1
print('po pętli')

# zbieranie danych cząstkowych
# najpierw przygotowujemy pusty kubelek
kubelek = 0
# w każdym obrocie pętli do kubelka dodaję
# kolejne liczby

# rozwiązanie wprost

t1 = int(input('podaj temp w 1. dzień'))
t2 = int(input('podaj temp w 2. dzień'))
t3 = int(input('podaj temp w 3. dzień'))
t4 = int(input('podaj temp w 4. dzień'))
t5 = int(input('podaj temp w 5. dzień'))
t6 = int(input('podaj temp w 6. dzień'))
t7 = int(input('podaj temp w 7. dzień'))

suma = t1+t2+t3+t4+t5+t6+t7
print(f'średnia temp to {suma/7:.2f}')

# rozwiązanie z pętlą
ile_dni = 7
nr_dnia = 1
suma_temp = 0
while nr_dnia <= ile_dni:
    suma_temp = suma_temp + int(input(f'podaj temp {nr_dnia}. dzień'))
    nr_dnia += 1

print(f'średnia temp to {suma_temp/ile_dni:.2f}')

