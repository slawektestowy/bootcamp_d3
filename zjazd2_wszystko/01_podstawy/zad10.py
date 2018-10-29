# + - * / ** // %

a = int(input('pierwsza liczba: '))
b = int(input('druga liczba: '))

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b)
operacja = input('operacja [+ - * /]: ')

print(f'przed stripem: #{operacja}#')
operacja = operacja.strip()
print(f'po stripie: #{operacja}#')

print('wynik działania: ', end='')
if operacja == '+':
    print(a+b)
elif operacja == '-':
    print(a - b)
elif operacja == '*':
    print(a * b)
elif operacja == '/':
    print(a / b)
elif operacja == '**':
    print(a ** b)
else:
    print(f'niepoprawny operator [{operacja}]')


