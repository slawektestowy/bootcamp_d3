# tupla to uporzadkowany ciag wartosci

para = (1,2)
trojka = ('ala','ma','kota')
czworka = (1, 'pies', (12,12),2.5)

print(para)

print(czworka[2])

print(len(trojka))  #ilosc elementow w danym obiekcie

print(czworka[1:2]) #przedzial

print(trojka[1:3])

print(czworka[0:3])

#jesli chcemy lapac od samego poczatku do samego konca to wystarczy zosrawic puste pole odpowiednio przed lub za :

print(czworka[-1]) #przedostatni element

print(czworka[-3:-1])

print(czworka[::2]) # skacze co drugi element

print(czworka[::-1])  #odwraca kolejnosc


