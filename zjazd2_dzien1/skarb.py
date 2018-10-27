from random import randint

# losujemy współrzędne gracza
gracz_x = randint(0, 9)
gracz_y = randint(0, 9)

#losujemy wspolrzedne skarbu
skarb_x = randint(0, 9)
skarb_y = randint(0, 9)
min_krokow = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)


print(f"Skarb ({skarb_x}, {skarb_y})")
ile_ruchow = 0
ruchow_lacznie = 0

while True:
    print(f"Pozycja gracza to ({gracz_x}, {gracz_y})")
    ruch = input("Podaj ruch: ")

    odleglosc_przed_ruchem = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)

    if ruch == 'w': #góra
        gracz_y += 1
    elif ruch == 's': #dół
        gracz_y -= 1
    elif ruch == 'd':  # prawo
        gracz_x += 1
    elif ruch == 'a':  # lewo
        gracz_x -= 1
    ile_ruchow += 1
    ruchow_lacznie += 1

    odleglosc_po_ruchu = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)

    if gracz_x >= 10 or gracz_x < 0 or gracz_y >= 10 or gracz_y < 0:
        print("Poza planszą!")
        break

#    if gracz_x == skarb_x and gracz_y == skarb_y:
    if odleglosc_po_ruchu == 0:
        print(f"Brawo, znalazłeś skarb w {ruchow_lacznie} ruchach!")
        break

    if ile_ruchow > 2 * min_krokow:
        skarb_x = randint(0, 9)
        skarb_y = randint(0, 9)
        min_krokow = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
        ile_ruchow = 0

    if randint(1, 100) > 20:
        if odleglosc_po_ruchu > odleglosc_przed_ruchem:
            print("Zimno!")
        else:
            print("Ciepło!")
