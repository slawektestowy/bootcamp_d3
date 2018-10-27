x = 1
y = 0
z = 0
while x <= 7:
    y = int(input(f'Podaj temperature w {x} dniu: '))
    x = x + 1
    z = z + y
print(z/7)



ile_dni=7
x = 1
y = 0

while x <= ile_dni:
    y = y + int(input(f'Podaj temperature w {x} dniu: '))
    x = x + 1

print(y/ile_dni)