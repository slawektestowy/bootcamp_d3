# plansza od 1 do 10
from random import random

#przygotowanie planszy
gracz_x = int(random() * 10) + 1
gracz_y = int(random() * 10) + 1

skarb_x = int(random() * 10) + 1
skarb_y = int(random() * 10) + 1

while True:
    print(f'pozycja gracza: ({gracz_x},{gracz_y})')

    odl_poprzednia = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
    ruch = input('podaj kierunek ruchu [p l g d]:')
    if ruch == 'p':
        gracz_x += 1
    elif ruch == 'l':
        gracz_x -= 1
    elif ruch == 'g':
        gracz_y -= 1
    elif ruch == 'd':
        gracz_y += 1

    if (gracz_x,gracz_y) == (skarb_x,skarb_y):
        print('Hurrra! skarb znaleziony!')
        exit(0)

    # if gracz_x == skarb_x and gracz_y == skarb_y:
    #     print('Hurrra! skarb znaleziony!')
    #     exit(0)

    if gracz_x < 1 or gracz_x > 10 or gracz_y < 1 or gracz_y > 10:
        print('spadłeś z planszy. nie żyjesz. hahaha!')
        exit(0)

    odl_po_ruchu = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
    if odl_poprzednia > odl_po_ruchu:
        print('ciepło')
    else:
        print('zimno')




