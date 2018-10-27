a = int(input('Podaj pierwsza liczbe: '))
b = int(input('Podaj druga liczbe: '))
d = input('podaj rodzaj operacji: ')

if d == ['+', '-', '*', '/']:
    if b == 0 and d == '/':
        print('blad dzielenia przez zero')
    else:
        if d == '+':
            print('Wynik: ', (a+b))
        elif d == '-':
            print('Wynik: ', (a-b))
        elif d == '*':
            print('Wynik: ', (a*b))
        elif d == '/':
            print('Wynik: ', (a/b))
else:
    print('blad operacji')