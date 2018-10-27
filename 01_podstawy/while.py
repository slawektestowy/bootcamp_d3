#while warunek kontynuacji
#    blok instrukcji
#
#1. przygotowanie zmiennej sterujacej
#2. zdefiniowanie warunku kontynuacji
#3. blok instrukcji
#4. wewnatrz bloku instrukcji zmieniamy zmienna sterujaca

i = 0
while i<10:
    print(i)
    i = i + 1

print('po petli')

i = i + 1  => i+=1