#napisz program ktory posortuje w tablicy przy wykorzystaniu algorytmu "sortowanie przez wybieranie"


l = [7, 10, 3, 2, 23]


for indeks_podstawienia in range(len(l)):
    print(f"Lista przed zmiana: {l}")
    min_index =None
    for i, liczba in enumerate(l[indeks_podstawienia:], indeks_podstawienia):
        if min_index is None or liczba < l[min_index]:
            min_index = i
    if min_index is None:
        break

#Zmien miejscami elementy

    l[min_index], l[indeks_podstawienia] = l[indeks_podstawienia], l[min_index]
    print(f"Lista po zmianie: {l}")
print(f"Po sortowaniu{l}")


# #print(min(l))
# # print(l.sort())
#
# max_index = None
# min_index = None
#
# for i, element in enumerate(l):   #znalezienie najmniejszego i najwiekszego indeksu
#     #print(element)
#     if max_index is None or l[max_index] < element:
#         max_index = i
#     if min_index is None or l[min_index] > element:
#         min_index = i
#
#
# print(f"Indeks maksymalnej wartośći to {max_index}")
# print(f"Indeks minimalnej wartośći to {min_index}")