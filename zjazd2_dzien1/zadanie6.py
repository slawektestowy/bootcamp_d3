lista = [3, 7, 123, -12, 47, 1, 0, 55, 18]


max_index = None
min_index = None

for i, element in enumerate(lista):
    #print(element)
    if max_index is None or lista[max_index] < element:
        max_index = i
    if min_index is None or lista[min_index] > element:
        min_index = i

if max_index is None:
    exit(0)

print(f"Indeks maksymalnej wartośći to {max_index}")
print(f"Indeks minimalnej wartośći to {min_index}")

print(lista)
#(lista[max_index], lista[min_index]) = (lista[min_index], lista[max_index])
# ^to robi to samo co 3 linijki ponizej
tmp = lista[max_index]
lista[max_index] = lista[min_index]
lista[min_index] = tmp

print(lista)