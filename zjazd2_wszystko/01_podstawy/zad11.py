# from random import random
#
# x = random() * 100 // 1
# x = round(random() * 100,0)


x = int(input('podaj pozycje X: '))
y = int(input('podaj pozycje Y: '))

if 0 <= x <= 10: # 0<=x and x<=10
    if 0 <= y <= 10:
        print("lewy górny róg")
    elif 10 < y < 90:
        print("lewy bok")
    elif 90 <= y <= 100:
        print("lewy dolny róg")
    else:
        print("jesteś poza planszą")
elif 10 < x < 90:
    if 0 <= y <= 10:
        print("górny bok")
    elif 10 < y < 90:
        print("środek")
    elif 90 <= y <= 100:
        print("dolny bok")
    else:
        print("jesteś poza planszą")
elif 90 <= x <= 100:
    if 0 <= y <= 10:
        print("prawy górny róg")
    elif 10 < y < 90:
        print("prawy bok")
    elif 90 <= y <= 100:
        print("prawy dolny róg")
    else:
        print("jesteś poza planszą")
else:
    print("jesteś poza planszą")

# alternatywne rozwiązanie

if 0 <= x <= 10:
    opis_x = 'lewy '
elif 90 <= x <=100:
    opis_x = 'prawy '
else:
    opis_x = ''

if 0 <= y <= 10:
    opis_y = 'górny '
elif 90 <= y <=100:
    opis_y = 'dolny '
else:
    opis_y = ''

if opis_x and opis_y:
    print(opis_x,opis_y,'róg', sep='')
elif opis_x or opis_y:
    print(opis_x,opis_y,'bok', sep='')
else:
    print('środek')