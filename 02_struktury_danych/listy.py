#listy mozna dynamicznie modyfikowac - tuple sa niemodyfikowalne

lista = [1,2,3,5]

print(lista[1])

print(lista[-1:-5:-2])

if 3 in lista:
    print('ok')

lista.append(6)
print(lista)

print(lista.count(3)) #pokazuje ile razy pojawia sie dany element

lista.insert(2,'ala ma kota')
print(lista)

del lista[5]

print(lista)