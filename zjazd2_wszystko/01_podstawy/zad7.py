x = int(input("podaj liczbę:"))

print(f'czy warunek: {not x % 2 != 0 and x % 3 == 0 and x > 10 or x ==7}')

print( True and True or False and False)
# hipoteza 1: or jest silniejszy
# True or False => True
# True and True and False => False

# hipoteza 2: and jest silniejszy
# True and True => True
# False and False => False
# True or False => True

# hipoteza 3: nie ma różnicy priorytetów
# True => True => False
