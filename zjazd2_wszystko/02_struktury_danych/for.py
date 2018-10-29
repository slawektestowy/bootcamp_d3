lista = [1,-2,3,4,-5,-6,7,8,-9,0]

# petla for przechodzi przez wszystkie elemety listy
# w kolejnych obrotach pętli zmienna el przechowuje
# kolejne wartości
for el in lista:
    print(el)

# uwaga na usuwanie elementów!
for el in lista:
    lista.remove(el)
    print(lista)

print(range(10))

for i in range(10):
    print(i)

