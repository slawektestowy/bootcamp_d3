# Napisz program wypisujacy na konsole zawartosc wskazanego pliku
# wraz z numerami linii. Obsłuz sytuacje, gdy uzytkownik nie poda
# nazwy pliku lub poda błedna nazwe.
# Przykład uzycia:
# $ python test.txt
# 1: pierwsza linia pliku
# 2: druga linia pliku

# with open('plik.txt', 'r') as f:
# #     dane = f.readline()  # czyta 1 linie
# #     print('1:',dane)
# #     dane = f.readlines(1)
# #     print('2:', dane)
# #     # dane = f.readline(2)
# #     # print('3:', dane)
# #     # dane = f.readline(3)
# #     # print('4:', dane)

# with open('zadanie.txt','r') as f:
#     linie = f.readlines()
#     print(f'1:{linie[0]} 2:{linie[1]} 3:{linie[2]} 4:{linie[3]}', sep='',end='\n')

# with open('zadanie.txt', 'r') as f:
#     linie = f.readlines()
#     for i, a in enumerate(linie):
#         print(linie)
# with open('zadanie.txt', 'r') as f:
#     linia = f.readline()
#     while linia:
#        linia = f.readline()
#        print(linia)
#
#     while True:
#         linia =f.readline()
#         if not linia:
#             break
#         print (f'{linia}')

# with open('zadanie.txt', 'r') as f:
#     i = 1
#     while True:
#         linia =f.readline()
#         if not linia:
#             break
#         print (f'{i}:{linia}', end="")
#         i +=1


# za pomoca enumerate
with open('zadanie.txt', 'r') as f:
    lista = f.readlines()
    for x, wart in enumerate(lista):
        print(f'{x+1}:{wart}', end="")