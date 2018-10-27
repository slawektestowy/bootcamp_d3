liczby = [1,-4,2,-90,13,15,-4,0]

ile_d = 0
ile_u = 0

for el in liczby:
    if el > 0:  # widzę liczbę dodatnią
        ile_d += 1  # zwiększam licznik dodatnich
    if el < 0:  # widzę liczbę dodatnią
        ile_u += 1  # zwiększam licznik dodatnich

print(f'na liście jest {ile_d} liczb dodatnich')
print(f'na liście jest {ile_u} liczb ujemnych')