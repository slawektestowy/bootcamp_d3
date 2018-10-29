pusta_lista = []
lista = [1,2,3,5,1,2,3,1,2]

print(lista[1])
print(lista[-1:-5:-2])
if 3 in lista:
    print('ok')

lista.append(6)#wstawianie na koniec
print(lista)
print(lista.count(1))

lista.insert(2,'ala ma kota')#wstawianie w środek
print(lista)

del lista[5]
print(lista)

lista.remove(2) #usuwa pierwszą znalezioną 2
print(lista)

lista.remove('ala ma kota')
print(lista)

lista.sort(reverse=True)
print(lista)

print('ala ma kota'.replace('a',''))

# del lista
# print(f'#{lista}#')