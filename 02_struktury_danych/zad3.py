lista = [1, -2, 3, 4, -5, -6, 7, 8, -9, 0]
lista2 = []
for el in lista:
    lista2.append(el >= 0)

print(lista2)


ile_d = 0
ile_u = 0
for el in lista:
    if el >0 :
        ile_d += 1
    else:
        ile_u += 1

print(f'na liscie jest {ile_d} liczb dodatnich')