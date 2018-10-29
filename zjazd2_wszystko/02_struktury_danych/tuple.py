# tupla (krotka)
# uporządkowany ciąg wartości

para = (1,2)
trójka = ('ala','ma','kota')
czwórka = (1,'pies',(12,12),2.5)

print(para)
print(czwórka[2]) #3. element
print(len(trójka)) #liczba elementów
print(czwórka[1:2])
print(trójka[1:3])
print(czwórka[0:3])
print(trójka[1:]) #do końca
print(czwórka[:3]) #od poczatku

print(czwórka[-1]) #ostatni element
print(czwórka[-3:-1])#3.i 2. od końca

print(czwórka[::2])#co ile elementów skakać
print(czwórka[::-1]) #w odwrotnej kolejności

tupla = (1,2,3,4,5,6,7,8,9,10)
print(tupla[1]) #drugi element
print(tupla[-2]) # przedostatni
print(tupla[2:7]) # od 3 do 7 włącznie
print(tupla[::3]) # co trzeci
print(tupla[::-2]) #co drugi od końca

if 14 in tupla:
    print('jest w tupli')
else:
    print('nie ma w tupli')

print(tupla.count(3)) # ile razy element wystepuje w tupli

#print(tupla[20]) #wyrzuca błąd IndexError
