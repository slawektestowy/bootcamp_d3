lista = []

while len(lista)<10:
    a = input('podaj liczbę: ')
    if a == '':
        break
    lista.append(int(a))

print(lista)
print('średnia:',sum(lista)/len(lista))